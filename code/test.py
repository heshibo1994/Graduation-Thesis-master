
# import math
# l = [-2.6295981,1.3237431,7.8566918],[],[],[-14.688413,3.8774083,7.7998452],[],[-6.0453339,6.3399105,7.4472828],[-9.8338594,7.1381879,7.4536138],[],[],[-5.1302309,10.444952,7.3042536],[-9.1714287,11.215644,7.2370219],[],[-0.32961807,13.559824,7.3419514],[],[],[-12.248101,16.149731,7.2656403]

# def fun(p1,p2):
# 	return round(math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2),2)

# for i in range(16):
# 	for j in range(i+1,16):
# 		if l[i] != [] and l[j]!=[]:
# 			print(i,j,fun(l[i],l[j]))

# print(12*math.sqrt(2))

# import xlrd
# temp = xlrd.open_workbook('2.xlsx') #打开路径为 ‘C:\\ww.xlsx’ 的excel
# table = temp.sheets()[0]  #打开temp中的第一个sheet页 [0]为索引值
# gpsx = []
# gpsy = []
# gpsz = []
# slamx = []
# slamy = []
# slamz = []

# for i in range(80,800):
# 	gpsx.append(table.row_values(i)[1]-6)
# 	gpsy.append(table.row_values(i)[3])
# 	gpsz.append(table.row_values(i)[5])
# 	slamx.append(table.row_values(i)[7])
# 	slamy.append(table.row_values(i)[9])
# 	slamz.append(table.row_values(i)[11])



# import matplotlib.pyplot as plt
# # 1.线图
# #调用plt。plot来画图,横轴纵轴两个参数即可
# plt.plot(gpsx,gpsy)
# # python要用show展现出来图
# #plt.show()


# plt.plot(gpsx,gpsy,  color='red', label='GPS',ls='-.')#ls或linestyle
# plt.plot(slamx,slamy, color='green', label='SLAM',ls=':')
# plt.legend()
 
# plt.xlabel('x')
# plt.ylabel('y')

# plt.show()


f = open("slam.txt")
temp = []
for i in f.readlines():
	temp+=([int(k)  for k in  i.split(" ")[:5]])
# print(temp)
stemp = list(set(temp))
stemp.sort()

dtemp = dict(zip(stemp,range(len(stemp))))


# f = open("slam.txt")
# for i in f.readlines():
# 	for j in  [int(k) for k in i.split(" ")[:1]]:
# 		print(dtemp[j],end = "&[")
# 	for j in  [int(k) for k in i.split(" ")[1:5]]:
# 		print(dtemp[j],end = " ")
# 	print(end = "")
# 	print("]&[")
# 	print(end = "")
# 	print(i.split("|")[1],end = "]")



a = 20000
total = 0
for i in range(1,13):
	gjj = a *0.24
	shuihou = a*0.77
	m = gjj+shuihou
	total = total + m
	print(i,m,total)
total = total + m*4*0.8
a = a*1.1
for i in range(13,25):
	gjj = a *0.24
	shuihou = a*0.77
	m = gjj+shuihou
	total = total + m
	print(i,m,total)
total = total + m*4*0.8
a = a*1.2
for i in range(25,37):
	gjj = a *0.24
	shuihou = a*0.77
	m = gjj+shuihou
	total = total + m
	print(i,m,total)
total = total + m*4*0.8
a = a*1.2
for i in range(37,49):
	gjj = a *0.24
	shuihou = a*0.77
	m = gjj+shuihou
	total = total + m
	print(i,m,total)
total = total + m*4*0.8
a = a*1.2
for i in range(49,61):
	gjj = a *0.24
	shuihou = a*0.77
	m = gjj+shuihou
	total = int(total + m)
	print(i,m,total)
total = total + m*4*0.8
print(total)

