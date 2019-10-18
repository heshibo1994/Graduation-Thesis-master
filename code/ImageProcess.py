import cv2


def sobel_demo(image):
    grad_x = cv2.Sobel(image, cv2.CV_32F, 1, 0)   #对x求一阶导
    grad_y = cv2.Sobel(image, cv2.CV_32F, 0, 1)   #对y求一阶导
    gradx = cv2.convertScaleAbs(grad_x)  #用convertScaleAbs()函数将其转回原来的uint8形式
    grady = cv2.convertScaleAbs(grad_y)
    cv2.imwrite("gradient_x.jpg", gradx)  #x方向上的梯度
    cv2.imwrite("gradient_y.jpg", grady)  #y方向上的梯度
    gradxy = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0) #图片融合
    cv2.imwrite("gradient.jpg", gradxy)

src = cv2.imread('ArUco.jpg')
cv2.namedWindow('input_image', cv2.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
cv2.imshow('input_image', src)
sobel_demo(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
