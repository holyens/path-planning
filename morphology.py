#19，形态学处理 
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import algorithms as alg
plt.rcParams['animation.ffmpeg_path']='D:/DevSoft/ffmpeg-win64-static/bin/ffmpeg'
##膨胀
def image_Dilate(image):
    print(image.shape)
    #将图像转化为灰度图像
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #对灰度图像进行二值化处理
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    #将二值化图像显示
    # cv.imshow("binary",binary)
    #设置形态学结构处理的核 矩形：MORPH_RECT; 交叉形：MORPH_CORSS; 椭圆形： MORPH_ELLIPSE;
    kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(10,10))
    #对二值图像进行膨胀操作
    dst=cv.dilate(binary,kernel)
    # cv.imshow("dilate_demo",dst)
    return dst

img = cv.imread('res/roadmap.png')


gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#对灰度图像进行二值化处理
ret,org=cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
#设置形态学结构处理的核 矩形：MORPH_RECT; 交叉形：MORPH_CORSS; 椭圆形： MORPH_ELLIPSE;
kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE, (10,10))
#对二值图像进行膨胀操作
dst=cv.dilate(org, kernel)
# np.savetxt('results/a.csv',dst, fmt='%d',delimiter=',')
start = (50,0)
goal = (50,999)
path = alg.astar(dst, start, goal)
path_x = [t[1] for t in path]
path_y = [t[0] for t in path]
fig1 = plt.figure()
plt.subplot(211),plt.imshow(255-org,'gray'),plt.title('ORIGIN')
plt.subplot(212),plt.imshow(255-dst,'gray') #,plt.plot(path_x,path_y,'--r'),plt.title('RESULT (%d,%d)->(%d,%d)'%(start[0],start[1],goal[0],goal[1]))
fig3 = plt.figure()
plt.imshow(255-org,'gray'),plt.plot(path_x,path_y,'--r'),plt.title('(%d,%d)->(%d,%d)'%(start[0],start[1],goal[0],goal[1]))
fig3.set_size_inches(20, 2)
# plt.plot([0,999],[50,50],'-.b')
line, = plt.plot(path_x[0],path_y[0], '.g',markersize=12)
def init():
    line.set_xdata(path_x[0])
    line.set_ydata(path_y[0])
    return line
def animate(i):
    line.set_xdata(path_x[i*2])
    line.set_ydata(path_y[i*2])
    return line
# Set up formatting for the movie files

ani = animation.FuncAnimation(fig=fig3,
                              func=animate,
                              frames=int(len(path_x)/2),
                              init_func=init,
                              interval=10,
                              blit=False)
##writer = animation.writers['ffmpeg']
##writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
mywriter = animation.FFMpegWriter()
ani.save('MovWave.mp4', writer=mywriter)
plt.show()



'''
# print(type(img))
# cv.namedWindow("src",0)
# cv.imshow("src",img)
# print(path)
# cv.waitKey(0)
# cv.destroyAllWindows() #使用Window name销毁指定窗口
# cv2.imwrite('messigray.png',img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
'''
##腐蚀
'''
def image_Erode(image):
    print(image.shape)
    #将图像转化为灰度图像
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #对灰度图像进行二值化处理
    ret,binary=cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    #将二值化图像显示
    cv.imshow("binary",binary)
    #设置形态学结构处理的核
    kernel=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    #对二值图像进行腐蚀操作
    dst=cv.erode(binary,kernel)
    cv.imshow("erode_demo",dst)
'''