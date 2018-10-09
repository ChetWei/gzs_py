from math import *

def isPrime(n):
    try:
        if isinstance(n,int):
            if n == 1:
                return False
            elif n == 2:
                return True
            for i in range(2, int(sqrt(n))+1):
                if n % i == 0:
                    return False
            return True
        else:
            print("参数类型错误")
            return False
    except:
        print("error")

print(isPrime(2))