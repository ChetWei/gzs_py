# -*- coding: utf-8 -*-
def rmb_to_dollar():
    rmb = input("请输入人民币金额:")
    rmb = float(rmb)
    dollar = rmb/6
    print("{rmb:.2f}人民币可兑换{dollar:.2f}美元".format(rmb=rmb,dollar=dollar))


def dollar_to_rmb():
    dollar = input("请输入美元金额:")
    dollar = float(dollar)
    rmb = dollar*6
    print("{dollar:.2f}美元可兑换{rmb:.2f}人民币".format(dollar=dollar,rmb=rmb))


if __name__ == "__main__":
    while True:
        num = input("1)人民币兑换美元请输入1\n2)美元兑换人民币请输入2\n3)退出请按q\n:")
        if num == '1':
            rmb_to_dollar()
        elif  num == '2':
            dollar_to_rmb()
        elif  num == 'q':
            print("退出...")
            break
        else:
            print("输入有误请重新输入:")

