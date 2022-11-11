import cv2
import numpy as np

from card_recognition.utils import scale_img, contour_image_rgb

img = cv2.imread('IMG_2960.jpg')

#scale down to certain pixel size


# resize image
resized = scale_img(img)

# contour_image_rgb(img, visualize=True)


gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
fltr_size = 1 + 2 * (min(resized.shape[0],
                         resized.shape[1]) // 20)
# thresh = cv2.adaptiveThreshold(gray,
#                                255,
#                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                cv2.THRESH_BINARY,
#                                fltr_size,
#                                10)
# else:
_, thresh = cv2.threshold(gray,
                          70,
                          255,
                          cv2.THRESH_BINARY)

cv2.imshow('card', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

_, contours, _ = cv2.findContours(
    np.uint8(thresh), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)





cv2.imshow('card', contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
