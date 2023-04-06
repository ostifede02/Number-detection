import cv2 as cv
import numpy as np
import os

resized_width = 130
resized_heigth = 140

def InitMaskImage(digit_value):
    mask_path = f"Images\\Mask\\Mask_{digit_value}.png"
    init_image_path = f"Images\\Training\\{digit_value}\\{digit_value}.{0}.png"
    init_mask = GetTrainingImage(init_image_path)
    cv.imwrite(mask_path, init_mask)
    return

def CreateMask(training_image, digit_value):
    mask_path = f"Images\\Mask\\Mask_{digit_value}.png"
    mask = cv.imread(mask_path)

    for i_row in range(0, resized_heigth):
        for j_col in range(0, resized_width):
            mask[i_row, j_col] = 0.9 * mask[i_row, j_col] + 0.1 * training_image[i_row, j_col]

    cv.imwrite(mask_path, mask)
    return

def GetTrainingImage(folder_path):

    raw_test_img = cv.imread(folder_path)
    gray_scale_img = cv.cvtColor(raw_test_img, cv.COLOR_RGB2GRAY)
    gray_scale_img_inverted = cv.bitwise_not(gray_scale_img)

    crop_img = CropImage(gray_scale_img_inverted)

    return crop_img

  

def CenterOfGravity(image):
    i_mass = 0
    j_mass = 0
    i_mass_total = 0
    j_mass_total = 0
    x_mass = 0
    y_mass = 0

    img_height = image.shape[0]
    img_width = image.shape[1]

    # calculating X-coordinate
    for j_col in range(0, img_width):
        j_mass = 0
        for i_row in range(0, img_height):
            j_mass += image[i_row, j_col] 

        x_mass += j_mass * j_col
        j_mass_total += j_mass
    
    X_cg = round(x_mass / j_mass_total)

    # calculating Y-coordinate
    for i_row in range(0, img_height):
        i_mass = 0
        for j_col in range(0, img_width):
            i_mass += image[i_row, j_col] 

        y_mass += i_mass * i_row
        i_mass_total += i_mass
    
    Y_cg = round(y_mass / i_mass_total)

    return (X_cg, Y_cg)


def CropImage(image):
    x1 = 0 
    x2 = 0
    y1 = 0
    y2 = 0
    mass = 0
    mass_mean = 0

    img_height = image.shape[0]
    img_width = image.shape[1]

    cg_img = CenterOfGravity(image)
    X_cg = cg_img[0]
    Y_cg = cg_img[1]

    # definig x1: left vertical crop rectangle
    for j_col in range(X_cg, -1, -1):
        mass = 0
        for i_row in range(0, img_height):
            mass += image[i_row, j_col]
        
        mass_mean = mass / img_height

        if mass_mean <= 0.02:
            mass = 0
            mass_mean = 0
            x1 = j_col
            break
    
    
    # definig x2: right vertical crop rectangle
    for j_col in range(X_cg, img_width):
        mass = 0
        for i_row in range(0, img_height):
            mass += image[i_row, j_col]
        
        mass_mean = mass / img_height

        if mass_mean <= 0.02:
            mass = 0
            mass_mean = 0
            x2 = j_col
            break
    
    
    # definig y1: top horizontal crop rectangle
    for i_row in range(Y_cg, -1, -1):
        mass = 0
        for j_col in range(0, img_width):
            mass += image[i_row, j_col]
        
        mass_mean = mass / img_width

        if mass_mean <= 0.02:
            mass = 0
            mass_mean = 0
            y1 = i_row
            break
    
    
    # definig y2: bottom horizontal crop rectangle
    for i_row in range(Y_cg, img_height):
        mass = 0
        for j_col in range(0, img_width):
            mass += image[i_row, j_col]
        
        mass_mean = mass / img_width

        if mass_mean <= 0.02:
            mass = 0
            mass_mean = 0
            y2 = i_row
            break
    
    cropped_image = cv.resize(image[y1:y2, x1:x2], (resized_width, resized_heigth))

    return cropped_image