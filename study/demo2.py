# -*- coding: utf-8 -*-
#绘制一条彩色蟒蛇，即在绘制Python蟒蛇的每个小段时，画笔的绘制颜色会发生变化
import turtle
import random
import time
def drawSnake(rad, angle, len, neckrad,sleep_time,color_list):
    '''
    :param rad: 半径
    :param angle: 弧度
    :param len:绘制次数
    :param neckrad:
    :param color_list: 颜色列表
    sleep_time : 睡眠时间
    :return:
    '''
    for i in range(len):
        turtle.pencolor(random.choice(color_list))
        turtle.circle(rad, angle)
        time.sleep(sleep_time)
        turtle.pencolor(random.choice(color_list))
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.forward(rad/2)  # 直线前进
    turtle.circle(neckrad, 180)
    turtle.forward(rad/4)



if __name__ == "__main__":
   turtle.setup(1500, 1400, 0, 0) #画布大小
   turtle.pensize(30)  # 画笔尺寸
   turtle.seth(-40)    # 前进的方向
   color_list = ['green','red','yellow','black','blue']
   drawSnake(70, 80, 10, 15,1,color_list)