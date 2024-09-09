import os
from typing import Any
import cv2
import numpy as np
import pytesseract

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

MIN_PERIMETER = 10
MIN_AREA = 300
SHOW_FIND_BIG_AREAS_STAGES = True
if SHOW_FIND_BIG_AREAS_STAGES:
    os.makedirs("results/find_big_areas_v1", exist_ok=True)

def find_big_areas(src: np.ndarray) -> list[tuple[np.ndarray, np.ndarray]]:
    """Эта функция ищет кадастровые кварталы (или как я их назвал большие участки)
    Кадастровый квартал - это участок, выделенный более толстой линией чем обычные участки
    Возвращает список из кортежей, состоящих из вырезанного цветного кадастрового квартала и его маску
    Для этого изображения преобразовываетя в HSV и убираются все цвета, кроме красного
    Этот метод не идеален, например для images/map_samples/download3.png функция не может выделить участки,
    из-за того, что не хватает буквального 1 пикселя для замыкания контура
    Как работает первая версия алгоритма есть в папке images/results/find_big_areas_v1
    """
    out: list[tuple[np.ndarray, np.ndarray]] = []
    src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    threshold = cv2.bitwise_or(cv2.inRange(
        src_hsv, np.array((0, 98, 0), dtype=np.uint8), np.array((5, 255, 255), dtype=np.uint8)
    ), cv2.inRange(
        src_hsv, np.array((177, 110, 0), dtype=np.uint8), np.array((179, 255, 176), dtype=np.uint8)
    ))
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
        cv2.fillPoly(contour_mask, [cnt], (255, ))
        if SHOW_FIND_BIG_AREAS_STAGES:
            cv2.imwrite(f"images/results/find_big_areas_v1/removed_blobs_{i}.png", removed_blobs)
        x, y, w, h = cv2.boundingRect(cnt)
        cropped = cv2.bitwise_and(src, src, mask=contour_mask)[y : y + h, x : x + w]
        if SHOW_FIND_BIG_AREAS_STAGES:
            cv2.imwrite(f"images/results/find_big_areas_v1/cropped_{i}.png", cropped)
        out.append((cropped, (cv2.bitwise_and(threshold, contour_mask))[y : y + h, x : x + w]))
        i += 1
        
    return out

def divide_big_area_to_smaller(big_area: tuple[np.ndarray, np.ndarray]) -> Any:
    """Эта функция должна находить участки внутри кадастрового квартала"""
    pass

def main():
    # проблема с download3.png
    image = cv2.imread("images/map_samples/download2.png")
    image_height = image.shape[0]
    image_width = image.shape[1]
    areas = find_big_areas(image)
    for i, images in enumerate(areas):
        cv2.imshow(f"cropped_{i}.png", images[0])
        cv2.imshow(f"threshold_{i}.png", images[1])

    cv2.waitKey()

if __name__ == "__main__":
    main()