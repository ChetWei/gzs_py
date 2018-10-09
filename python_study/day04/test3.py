# -*- coding: utf-8 -*-

month_put = 3000    #第一个月的投入
month_get = 0       #第一个月的利息

for month in range(120):
    month_get = month_put*0.01  #第二个月获得的利息
    month_put += 3000   #第二个月的投入,假设上一个月的利息没有投入            
    
times = (month_get + 5000) / 5000  
    
print("10年后小红的月收入{},其中理财收入{},工资收入{}".format(month_get+5000,month_get,5000))
print("小红收入是小明的{}倍 ".format(times) )  