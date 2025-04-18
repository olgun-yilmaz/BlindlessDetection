import cv2
import numpy as np


def apply_preprocessing(img, img_size=96):
    img = cv2.resize(img, (img_size, img_size))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 10, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return img_rgb

    contour = max(contours, key=cv2.contourArea)[:, 0, :]

    x1 = np.min(contour[:, 0])
    y1 = np.min(contour[:, 1])
    x2 = np.max(contour[:, 0])
    y2 = np.max(contour[:, 1])

    h, w = img_rgb.shape[:2]
    if (x2 - x1 > w // 6) and (y2 - y1 > h // 6):
        x_margin = (x2 - x1) * 4 // 50
        y_margin = (y2 - y1) * 5 // 50
        cropped = img_rgb[y1 + y_margin : y2 - y_margin, x1 + x_margin : x2 - x_margin]
        cropped = cv2.resize(cropped, (img_size, img_size))
    else:
        cropped = img_rgb.copy()

    lab = cv2.cvtColor(cropped, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    lab_clahe = cv2.merge((cl, a, b))
    img_clahe = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2RGB)

    med_blur = cv2.medianBlur(img_clahe, 3)
    background = cv2.medianBlur(img_clahe, 37)

    mask = cv2.subtract(med_blur, background)
    mask = cv2.normalize(mask, None, 0, 255, cv2.NORM_MINMAX)
    final_img = cv2.bitwise_and(mask, med_blur)

    return final_img
