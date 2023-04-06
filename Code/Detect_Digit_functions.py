def CheckAffinity(mask_img_value, mask_img, test_img):
    img_width = test_img.shape[0]
    img_heigth = test_img.shape[1]

    accuracy_counter = 0

    for i_row in range(0, img_width):
        for j_col in range(0, img_heigth):
            if test_img[i_row, j_col] >= 10:       # if pixel in image is part of the digit
                mask_img_mass = mask_img[i_row, j_col][0]

                if mask_img_mass >= 200:
                    accuracy_counter += 3
                
                elif (mask_img_mass >= 120) and (mask_img_mass < 200):
                    accuracy_counter += 1
                
                elif mask_img_mass < 50:
                    accuracy_counter -= 2

                else:
                    accuracy_counter += 0

    return [mask_img_value, accuracy_counter]