import cv2
import numpy as np

img = cv2.imread('images/girl.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (650,450))

def nothing(s):
  pass

# extracting colorcode
cv2.namedWindow('Color Adjustments')
cv2.resizeWindow('Color Adjustments', 300,300)
cv2.createTrackbar('Scale', 'Color Adjustments', 0, 255, nothing)
cv2.createTrackbar('Color', 'Color Adjustments', 0, 255, nothing)

while True:
  scale = cv2.getTrackbarPos('Scale', 'Color Adjustments')
  color = cv2.getTrackbarPos('Color', 'Color Adjustments')

  inverted_gray = color - gray
  blur_img = cv2.GaussianBlur(inverted_gray, (21,21), 0)
  inverted_blur = color - blur_img
  fltr = cv2.divide(gray, inverted_blur, scale=scale)


  cv2.imshow('girl', fltr)
  k= cv2.waitKey(1)
  if k == ord('q'):
    break
  if k ==ord('s'):
    cv2.imwrite('res.jpg', fltr)