# -*- coding: utf-8 -*-

days = int(input("请输入持续学习时间:"))

remain = days % 7
weeks = days // 7

print('可以持续学习{weeks}个星期,剩余{remain}天'.format(weeks=weeks,remain=remain))

week_improve = 1.01**4

last_improve = 1
if remain > 3:
    last_improve = (remain-3) * 1.01 

total_improve = week_improve**weeks * last_improve

print ("连续学习{days}天之后，能力值为:{total_improve}".format(days=days,total_improve=total_improve))