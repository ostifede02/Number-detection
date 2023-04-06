import cv2 as cv
import Image_Processing_functions as process_fnc
import Detect_Digit_functions as detect_fnc

digit_value = 2
test_image_index = 0

test_img_path = f"Images\\Test\\{digit_value}\\T{digit_value}.{test_image_index}.png"
test_img = process_fnc.GetTrainingImage(test_img_path)

detected_affinity = -1000000

for mask_index in range(0, 6):

    mask_img = cv.imread(f"Images\\Mask\\Mask_{mask_index}.png")
    affinity_result = detect_fnc.CheckAffinity(mask_index, mask_img, test_img)
    print(affinity_result)

    if affinity_result[1] >= detected_affinity:
        detected_digit = affinity_result[0]
        detected_affinity = affinity_result[1]

print(f"The digit detected is: {detected_digit}")

mask_img = cv.imread(f"Images\\Mask\\Mask_{detected_digit}.png")
cv.imshow("mask", mask_img)
cv.imshow("test", test_img)

cv.waitKey(0)