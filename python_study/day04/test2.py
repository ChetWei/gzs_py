# -*- coding: utf-8 -*-


import time
point=11
print("--------执行开始----------")
for i in range(point):
    start ="Staring"
    done="Done!"
    process='.'*i
    print("{}{}".format(start,process))
    if i == point-1:
        print("{}{}{}".format(start,process,done))
    time.sleep(0.5)
print("--------执行结束----------")
