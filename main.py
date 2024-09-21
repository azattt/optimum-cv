import os
import random
import cv2
import numpy as np
# import pytesseract


# Эта часть использовалась для тестирования распознования номеров участков, но она не заработала, так как
# не находила все цифры
# USE_TESSERACT = False
# if USE_TESSERACT:
#     # нужно скачивать tesseract-ocr и вставлять путь сюда
#     pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract-ocr\tesseract.exe"

#     def find_digits_tesseract(im):
#         out = np.copy(im)
#         data = pytesseract.image_to_boxes(
#             out, output_type=pytesseract.Output.DICT, config="--psm 11 digits"
#         )
#         if "char" in data:
#             for i, char in enumerate(data["char"]):
#                 cv2.rectangle(
#                     out,
#                     (data["left"][i], im.shape[0] - data["top"][i]),
#                     (data["right"][i], im.shape[0] - data["bottom"][i]),
#                     (0, 255, 0),
#                     2,
#                 )
#                 cv2.putText(
#                     out,
#                     char,
#                     (data["left"][i], im.shape[0] - data["top"][i]),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     0.5,
#                     (0, 255, 0),
#                 )
#         return out

MIN_PERIMETER = 10
MIN_AREA = 300
SHOW_FIND_BIG_AREAS_STAGES = True
if SHOW_FIND_BIG_AREAS_STAGES:
    os.makedirs("images/results/find_big_areas_v1", exist_ok=True)


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
    # if SHOW_FIND_BIG_AREAS_STAGES:
    #     cv2.imwrite("images/results/find_big_areas_v1/removed_blobs.png", removed_blobs)
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
    big_area: tuple[np.ndarray, np.ndarray], trackbar_value: int
) -> np.ndarray:
    """Эта функция должна находить участки внутри кадастрового квартала"""
    image = big_area[1].copy()
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    removed_blobs = cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel)
    contours, hierarchy_outer = cv2.findContours(
        removed_blobs, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE
    )
    hierarchy = hierarchy_outer[0]
    # next_index = 884
    image_with_contours_colored = np.zeros((*image.shape, 3), dtype=np.uint8)
    colors: set[tuple[int, int, int, int]] = set()
    random.seed(4)
    max_arc_length = 0.0
    # index_with_max_arc_length = 0
    # Похоже, что контур с самым большим периметром - последний контур в текущем уровне иерархии

    # 884 885 1105
    indices: list[int] = [i for i in range(len(hierarchy)) if hierarchy[i][3] == 884]
    # indices.append(0)
    indices.append(884)
    # indices = [trackbar_value]
    # index_with_max_arc_length = 0
    # while hierarchy[next_index][0] != -1:
    #     next_index = int(hierarchy[next_index][0])
    #     indices.append(next_index)
    print([hierarchy[i] for i in indices])
    # color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color = (0, 255, 0)
    # cv2.polylines(image_with_contours_colored, [contours[i] for i in indices], False, color)
    # for contour in contours[2:30]:
        # cv2.fillPoly(image_with_contours_colored, [contour], color)
    cv2.fillPoly(image_with_contours_colored, [contours[i] for i in indices], color)
    result = cv2.addWeighted(big_area[0], 1.0, image_with_contours_colored, 0.5, 0)
    cv2.imshow("result", result)
    # while next_index != -1:
    #     # print(next_index)
    #     
    #     while color in colors:
    #         color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
    #     colors.add(color)
    #     print(next_index)
    #     arcLength = cv2.arcLength(contours[next_index], False)
    #     if arcLength > max_arc_length:
    #         max_arc_length = arcLength
    #         index_with_max_arc_length = next_index
    #     cv2.polylines(image_with_contours_colored, [contours[next_index]], False, color)
    #     next_index = hierarchy[next_index][0]

    # print(max_arc_length, index_with_max_arc_length)
    cv2.imshow("image_with_contours_colored", image_with_contours_colored)

    # random.seed(4)
    # children: Queue[int] = Queue()
    # next_contour_index = 0
    # level = 0
    # indices = []
    # while next_contour_index != -1 or not children.empty():
    #     if next_contour_index == -1:
    #         next_contour_index = children.get()
    #         # print("going down at", next_index)
    #         level += 1

    #     indices.append(int(next_contour_index))
    #     cnt = contours[next_contour_index]
        
    #     if True or cv2.contourArea(cnt) >= 200 and cv2.arcLength(cnt, True) >= 200:
    #         # print(level, show_level)
    #         if level == show_level:
    #             # print(level, next_contour_index)
    #             color = (
    #                 random.randint(100, 255),
    #                 random.randint(100, 255),
    #                 random.randint(100, 255),
    #             )
    #             cv2.fillPoly(image_with_contours_colored, [cnt], color)
    #             cv2.polylines(image_with_contours_colored, [cnt], False, color)

    #     if hierarchy[next_contour_index][2] != -1:
    #         children.put(hierarchy[next_contour_index][2])

    #     next_contour_index = hierarchy[next_contour_index][0]

    # cv2.imshow("image_with_contours_colored", image_with_contours_colored)

    return image



# Тестовый код, нужно убрать
class Test:
    def __init__(self, show_level: int, images: tuple[np.ndarray, np.ndarray]):
        self.trackbar_value = show_level
        self.images = images
        cv2.namedWindow("image_with_contours_colored")
        cv2.resizeWindow("image_with_contours_colored", 1500, 0)
        cv2.createTrackbar("value", "image_with_contours_colored", 0, 1143, self.set_trackbar_value)
        self.draw()

    def set_trackbar_value(self, trackbar_value: int = 0):
        self.trackbar_value = trackbar_value
        self.draw()
    
    def draw(self):
        divide_big_area_to_smaller(self.images, self.trackbar_value)
        # cv2.imshow(f"cropped_{0}.png", self.images[0])

def main():
    # проблема с download2.png
    image = cv2.imread("images/map_samples/download2.png")
    image_height = image.shape[0]
    image_width = image.shape[1]
    areas = find_big_areas(image)
    # test = Test(0, areas[0])
    # for i, images in enumerate(areas):
    #     colored_contours = divide_big_area_to_smaller(images, main.show_level)
    #     cv2.imshow(f"colored_contours_{i}", colored_contours)
    #     cv2.imshow(f"cropped_{i}.png", images[0])
    #     cv2.imshow(f"threshold_{i}.png", images[1])

    cv2.waitKey()


if __name__ == "__main__":
    main()
