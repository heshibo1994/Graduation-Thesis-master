# import cv2
# from PIL import Image

# # def sobel_demo(image):
# #     grad_x = cv2.Sobel(image, cv2.CV_32F, 1, 0)   #对x求一阶导
# #     grad_y = cv2.Sobel(image, cv2.CV_32F, 0, 1)   #对y求一阶导
# #     gradx = cv2.convertScaleAbs(grad_x)  #用convertScaleAbs()函数将其转回原来的uint8形式
# #     grady = cv2.convertScaleAbs(grad_y)
# #     cv2.imwrite("gradient_x.jpg", gradx)  #x方向上的梯度
# #     cv2.imwrite("gradient_y.jpg", grady)  #y方向上的梯度
# #     gradxy = cv2.addWeighted(gradx, 0.5, grady, 0.5, 0) #图片融合
# #     cv2.imwrite("gradient.jpg", gradxy)

# # src = cv2.imread('ArUco.jpg')
# # cv2.namedWindow('input_image', cv2.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
# # #cv2.imshow('input_image', src)
# # sobel_demo(src)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()


# p = cv2.imread("gradient.jpg")
# img_gray = cv2.cvtColor(p,cv2.COLOR_RGB2GRAY)
# cv2.imwrite("gradientimg_gray.jpg",img_gray)

# im  =Image.open('gradientimg_gray.jpg')#打开图片
# for i in range(im.width):
# 	print(i)
# 	for j in range(im.height):
# 		im.putpixel((i,j),255-im.getpixel((i,j)))#修改像素，第一个参数是元组
# im2 =im.resize((730,961))#改变图片大小
# im2.save('gradientimg_gray_2.png')#改变图片格式
