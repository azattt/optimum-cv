import os
from queue import Queue
import random
from typing import Any
import cv2
import numpy as np
import pytesseract

import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout


# Эта часть использовалась для тестирования распознования номеров участков, но она не заработала, так как
# не находила все цифры
USE_TESSERACT = False
if USE_TESSERACT:
    # нужно скачивать tesseract-ocr и вставлять путь сюда
    pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract-ocr\tesseract.exe"

    def find_digits_tesseract(im):
        out = np.copy(im)
        data = pytesseract.image_to_boxes(
            out, output_type=pytesseract.Output.DICT, config="--psm 11 digits"
        )
        if "char" in data:
            for i, char in enumerate(data["char"]):
                cv2.rectangle(
                    out,
                    (data["left"][i], im.shape[0] - data["top"][i]),
                    (data["right"][i], im.shape[0] - data["bottom"][i]),
                    (0, 255, 0),
                    2,
                )
                cv2.putText(
                    out,
                    char,
                    (data["left"][i], im.shape[0] - data["top"][i]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                )
        return out


# взято из https://stackoverflow.com/a/20831563
def neighbours_vec(image):
    return (
        image[2:, 1:-1],
        image[2:, 2:],
        image[1:-1, 2:],
        image[:-2, 2:],
        image[:-2, 1:-1],
        image[:-2, :-2],
        image[1:-1, :-2],
        image[2:, :-2],
    )


def transitions_vec(P2, P3, P4, P5, P6, P7, P8, P9):
    return (
        ((P3 - P2) > 0).astype(int)
        + ((P4 - P3) > 0).astype(int)
        + ((P5 - P4) > 0).astype(int)
        + ((P6 - P5) > 0).astype(int)
        + ((P7 - P6) > 0).astype(int)
        + ((P8 - P7) > 0).astype(int)
        + ((P9 - P8) > 0).astype(int)
        + ((P2 - P9) > 0).astype(int)
    )


def zhangSuen_vec(image, iterations):
    for iter in range(1, iterations):
        print(iter)
        # step 1
        P2, P3, P4, P5, P6, P7, P8, P9 = neighbours_vec(image)
        condition0 = image[1:-1, 1:-1]
        condition4 = P4 * P6 * P8
        condition3 = P2 * P4 * P6
        condition2 = transitions_vec(P2, P3, P4, P5, P6, P7, P8, P9) == 1
        condition1 = (2 <= P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9) * (
            P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9 <= 6
        )
        cond = (
            (condition0 == 1)
            * (condition4 == 0)
            * (condition3 == 0)
            * (condition2 == 1)
            * (condition1 == 1)
        )
        changing1 = np.where(cond == 1)
        image[changing1[0] + 1, changing1[1] + 1] = 0
        # step 2
        P2, P3, P4, P5, P6, P7, P8, P9 = neighbours_vec(image)
        condition0 = image[1:-1, 1:-1]
        condition4 = P2 * P6 * P8
        condition3 = P2 * P4 * P8
        condition2 = transitions_vec(P2, P3, P4, P5, P6, P7, P8, P9) == 1
        condition1 = (2 <= P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9) * (
            P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9 <= 6
        )
        cond = (
            (condition0 == 1)
            * (condition4 == 0)
            * (condition3 == 0)
            * (condition2 == 1)
            * (condition1 == 1)
        )
        changing2 = np.where(cond == 1)
        image[changing2[0] + 1, changing2[1] + 1] = 0
    return image


MIN_PERIMETER = 10
MIN_AREA = 300
SHOW_FIND_BIG_AREAS_STAGES = True
if SHOW_FIND_BIG_AREAS_STAGES:
    os.makedirs("results/find_big_areas_v1", exist_ok=True)


def find_big_areas(src: np.ndarray) -> list[tuple[np.ndarray, np.ndarray]]:
    """Эта функция ищет кадастровые кварталы (или как я их назвал большие участки)
    Кадастровый квартал - это участок, выделенный более толстой линией чем обычные участки
    Возвращает список из кортежей, состоящих из вырезанного цветного кадастрового квартала и его маску
    Для этого, изображение преобразовываетcя в HSV и убираются все цвета, кроме красного
    Этот метод не идеален, например для images/map_samples/download3.png функция не может выделить участки,
    из-за того, что не хватает буквального 1 пикселя для замыкания контура
    Как работает первая версия алгоритма есть в папке images/results/find_big_areas_v1
    """
    out: list[tuple[np.ndarray, np.ndarray]] = []
    src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    threshold = cv2.bitwise_or(
        cv2.inRange(
            src_hsv, np.array((0, 98, 0), dtype=np.uint8), np.array((5, 255, 255), dtype=np.uint8)
        ),
        cv2.inRange(
            src_hsv,
            np.array((177, 110, 0), dtype=np.uint8),
            np.array((179, 255, 176), dtype=np.uint8),
        ),
    )
    if SHOW_FIND_BIG_AREAS_STAGES:
        cv2.imwrite("images/results/find_big_areas_v1/threshold.png", threshold)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    removed_blobs = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    if SHOW_FIND_BIG_AREAS_STAGES:
        cv2.imwrite("images/results/find_big_areas_v1/removed_blobs.png", removed_blobs)
    contours, _ = cv2.findContours(removed_blobs, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    i = 0
    for cnt in contours:
        if cv2.arcLength(cnt, True) < MIN_PERIMETER:
            continue
        if cv2.contourArea(cnt, True) < MIN_AREA:
            continue
        if cv2.arcLength(cnt, True) > cv2.contourArea(cnt, True):
            continue

        contour_mask = np.zeros(src.shape[:-1], dtype=np.uint8)
        cv2.fillPoly(contour_mask, [cnt], (255,))
        if SHOW_FIND_BIG_AREAS_STAGES:
            cv2.imwrite(f"images/results/find_big_areas_v1/removed_blobs_{i}.png", removed_blobs)
        x, y, w, h = cv2.boundingRect(cnt)
        cropped = cv2.bitwise_and(src, src, mask=contour_mask)[y : y + h, x : x + w]
        if SHOW_FIND_BIG_AREAS_STAGES:
            cv2.imwrite(f"images/results/find_big_areas_v1/cropped_{i}.png", cropped)
        out.append((cropped, (cv2.bitwise_and(threshold, contour_mask))[y : y + h, x : x + w]))
        i += 1

    return out


def divide_big_area_to_smaller(
    big_area: tuple[np.ndarray, np.ndarray], show_level: int
) -> np.ndarray:
    """Эта функция должна находить участки внутри кадастрового квартала"""
    image = big_area[1].copy()
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    removed_blobs = cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel)
    contours, hierarchy_outer = cv2.findContours(
        removed_blobs, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE
    )
    hierarchy = hierarchy_outer[0]

    image_with_contours_colored = np.zeros((*image.shape, 3), dtype=np.uint8)

    random.seed(4)
    children: Queue[int] = Queue()
    next_contour_index = 0
    level = 0
    indices = []
    while next_contour_index != -1 or not children.empty():
        if next_contour_index == -1:
            next_contour_index = children.get()
            # print("going down at", next_index)
            level += 1

        indices.append(int(next_contour_index))
        cnt = contours[next_contour_index]
        
        if True or cv2.contourArea(cnt) >= 200 and cv2.arcLength(cnt, True) >= 200:
            # print(level, show_level)
            if level == show_level:
                # print(level, next_contour_index)
                color = (
                    random.randint(100, 255),
                    random.randint(100, 255),
                    random.randint(100, 255),
                )
                cv2.fillPoly(image_with_contours_colored, [cnt], color)
                cv2.polylines(image_with_contours_colored, [cnt], False, color)

        if hierarchy[next_contour_index][2] != -1:
            children.put(hierarchy[next_contour_index][2])

        next_contour_index = hierarchy[next_contour_index][0]

    cv2.imshow("image_with_contours_colored", image_with_contours_colored)

    return image



# Тестовый код, нужно убрать
class Test:
    def __init__(self, show_level: int, images: tuple[np.ndarray, np.ndarray]):
        self.show_level = show_level
        self.images = images

    def set_show_level(self, show_level: int = 0):
        self.show_level = show_level
        self.draw()
    
    def draw(self):
        divide_big_area_to_smaller(self.images, self.show_level)
        # cv2.imshow(f"cropped_{0}.png", self.images[0])

def main():
    
    # проблема с download2.png
    image = cv2.imread("images/map_samples/download.png")
    image_height = image.shape[0]
    image_width = image.shape[1]
    areas = find_big_areas(image)
    test = Test(0, areas[0])
    cv2.namedWindow("image_with_contours_colored")
    cv2.createTrackbar("show_level", "image_with_contours_colored", 0, 400, test.set_show_level)
    # for i, images in enumerate(areas):
    #     colored_contours = divide_big_area_to_smaller(images, main.show_level)
    #     cv2.imshow(f"colored_contours_{i}", colored_contours)
    #     cv2.imshow(f"cropped_{i}.png", images[0])
    #     cv2.imshow(f"threshold_{i}.png", images[1])

    cv2.waitKey()


if __name__ == "__main__":
    main()
