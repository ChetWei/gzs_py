import random

NUMBER = random.randint(0,100)
print("随机生成数字",NUMBER)
GUESS_TIMES = 0

while True :
    guess = input("请猜测整数(范围0~100)")
    try:
        guess = int(guess)
        GUESS_TIMES += 1
        if guess == NUMBER:
            print("预测{0}次，你猜中了！".format(GUESS_TIMES))
            break
        elif guess > NUMBER:
            print("遗憾，太大了！")
        elif guess < NUMBER:
            print("遗憾，太小了！")
    except ValueError:
        print("输入内容必须为整数")