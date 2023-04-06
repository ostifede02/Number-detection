import cv2 as cv
import Image_Processing_functions as fnc

for digit_value in range(0, 6):
    fnc.InitMaskImage(digit_value)

    for image_index in range(1, 10):

        folder_path = f"Images\\Training\\{digit_value}\\{digit_value}.{image_index}.png"

        training_img = fnc.GetTrainingImage(folder_path)
        fnc.CreateMask(training_img, digit_value)

print("Training ended succesfully!")