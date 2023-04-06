import cv2
import numpy 
 
originalImage = cv2.imread("Images\\Training\\3\\3.0.png")
ROI = cv2.selectROI("original Image", originalImage)

print(ROI)

x1 = ROI[0]
y1 = ROI[1]
x2 = ROI[2]
y2 = ROI[3]

print(type(x1))
print(x1)

slicedImage = originalImage[y1:y2, x1:x2]

print(slicedImage)
 
cv2.imshow("Original Image", originalImage)
cv2.imshow("Sliced Image", slicedImage)
 
cv2.waitKey(0)
cv2.destroyAllWindows()