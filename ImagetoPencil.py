
import cv2
image=cv2.imread("dog.jpg", cv2.IMREAD_COLOR)
cv2.imshow('Orig', image)
cv2.waitKey(0)

#first we gray scale the original image
gray_scale=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray', gray_scale)
cv2.waitKey(0)

# invert the grayscale image for the inverted image
#converting with negative
negative=cv2.bitwise_not(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
#ret, thrsh=cv2.threshold(gray_scale, 127, 200, cv2.THRESH_TOZERO)
#thrsh=cv2.adaptiveThreshold(gray_scale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)
#negative= cv2.bitwise_not(thrsh)
cv2.imshow('negative', negative)
cv2.waitKey(0)

# blend the gray scale image with the inverted blurry image
# we will blend dirst with median blur
blur=cv2.GaussianBlur(negative, (21,21),0)
cv2.imshow('blur', blur)
cv2.waitKey(0)

divide= cv2.divide(gray_scale,blur,scale=255)
cv2.imshow('sketch', divide)
cv2.waitKey(0)


cv2.destroyAllWindows()