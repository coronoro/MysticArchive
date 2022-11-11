import cv2
import numpy as np


def contour_image(self, full_image, mode='gray'):
    """
    Wrapper for selecting the countouring / thresholding algorithm
    """
    if mode == 'gray':
        contours = self.contour_image_gray(full_image,
                                           thresholding='simple')
    elif mode == 'adaptive':
        contours = self.contour_image_gray(full_image,
                                           thresholding='adaptive')
    elif mode == 'rgb':
        contours = self.contour_image_rgb(full_image)
    elif mode == 'all':
        contours = self.contour_image_gray(full_image,
                                           thresholding='simple')
        contours += self.contour_image_gray(full_image,
                                            thresholding='adaptive')
        contours += self.contour_image_rgb(full_image)
    else:
        raise ValueError('Unknown segmentation mode.')
    contours_sorted = sorted(contours, key=cv2.contourArea, reverse=True)
    return contours_sorted


def contour_image_rgb(img, visualize=False):
    """
    Grayscale transform, thresholding, countouring and sorting by area.
    """
    clahe = cv2.createCLAHE(clipLimit=2.0,
                                 tileGridSize=(8, 8))
    blue, green, red = cv2.split(img)
    blue = clahe.apply(blue)
    green = clahe.apply(green)
    red = clahe.apply(red)
    _, thr_b = cv2.threshold(blue, 110, 255, cv2.THRESH_BINARY)
    _, thr_g = cv2.threshold(green, 110, 255, cv2.THRESH_BINARY)
    _, thr_r = cv2.threshold(red, 110, 255, cv2.THRESH_BINARY)
    _, contours_b, _ = cv2.findContours(np.uint8(thr_b), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    _, contours_g, _ = cv2.findContours(
        np.uint8(thr_g), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    _, contours_r, _ = cv2.findContours(
        np.uint8(thr_r), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours_b + contours_g + contours_r
    if visualize:
        cv2.imshow(thr_r)
        cv2.show()
        cv2.imshow(thr_g)
        cv2.show()
        cv2.imshow(thr_b)
        cv2.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return contours



def scale_img(img, scale_width=1000):
    scale_percent = (scale_width * 100) / img.shape[1]
    height = int(img.shape[0] * scale_percent / 100)
    dim = (scale_width, height)
    return cv2.resize(img, dim)
