import numpy as np
import cv2

def converter (blue, green, red) :

    color = np.uint8([[[blue, green, red]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    hue = hsv_color[0][0][0]

    print("Lower bound is :"),
    print("[" + str(hue - 10) + ", 100, 100]\n")

    print("Upper bound is :"),
    print("[" + str(hue + 10) + ", 255, 255]")


converter(120,238,5)

def OpenCV():
    img = cv2.imread('circles.jpeg', 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_range_red = np.array([167, 100, 100], dtype=np.uint8)
    upper_range_red = np.array([187, 255, 255], dtype=np.uint8)

    lower_range_blue = np.array([106, 100, 100], dtype=np.uint8)
    upper_range_blue = np.array([126, 255, 255], dtype=np.uint8)

    lower_range_green = np.array([65, 100, 100], dtype=np.uint8)
    upper_range_green = np.array([85, 255, 255], dtype=np.uint8)



    mask_red = cv2.inRange(hsv, lower_range_red, upper_range_red)
    mask_blue = cv2.inRange(hsv, lower_range_blue, upper_range_blue)
    mask_green = cv2.inRange(hsv, lower_range_green, upper_range_green)


    cv2.imshow('mask_red', mask_red)
    cv2.imshow('mask_blue', mask_blue)
    cv2.imshow('mask_green', mask_green )

    cv2.imshow('image', img)




    while 1:
        k = cv2.waitKey(0)
        if k == 27:
            break

    cv2.destroyAllWindows()

