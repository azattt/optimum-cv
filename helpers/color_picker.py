import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract-ocr\tesseract.exe"

def nothing(_):
    pass

def rotate_image(img, angle):
    img_center = tuple(np.array(img.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(img_center, angle, 1.0)
    res = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)
    return res

# Load image
image = cv2.imread('cropped.png')
# image = rotate_image(image, 75)

# image = cv2.resize(image, None, fx=10, fy=10)
# sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
# image = cv2.filter2D(image, -1, sharpen_kernel)
image_height = image.shape[0]
# Create a window
cv2.namedWindow('image')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', 'image', 0, 179, nothing)
cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'image', 179)
cv2.setTrackbarPos('SMax', 'image', 255)
cv2.setTrackbarPos('VMax', 'image', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while(1):
    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'image')
    sMin = cv2.getTrackbarPos('SMin', 'image')
    vMin = cv2.getTrackbarPos('VMin', 'image')
    hMax = cv2.getTrackbarPos('HMax', 'image')
    sMax = cv2.getTrackbarPos('SMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow("mask", mask)
    result = cv2.bitwise_and(image, image, mask=mask)
    # data = pytesseract.image_to_boxes(mask, output_type=pytesseract.Output.DICT, config='--psm 11 digits')
    # if 'char' in data:
    #     for i, char in enumerate(data['char']):
    #         cv2.rectangle(result, (data['left'][i], image_height-data['top'][i]), (data['right'][i], image_height-data['bottom'][i]), (100, 100, 100), 2)
    #         cv2.putText(result, char, (data['left'][i], image_height-data['top'][i]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display result image
    # cv2.imshow('image', result)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()