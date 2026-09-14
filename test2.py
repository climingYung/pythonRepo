#test파일에 있는 add, multi함수를 호출하고 싶음
from  test import add , multi
#add, multi함수가 test모듈에 있기 때문에 일단 불러봐야함

#import 모듈이름
#from 모듈이름 import 함수 이름 -> 모듈에서 필요한 함수만 가져올 때

#from 모듈이름 import *
#모듈안에 있는 함수 모두 가져올 때 *

print(add(1,2))
print(multi(10,5))


#참과 거짓 예측
all([1,2, abs(-3),-3]) #True
chr(ord("a")) == "a" #True 두번 바뀌어서 a = a


#음수 제거
print(list(filter(lambda x : x > 0, [1, -2, 3, -5, 8, -3])))

#최댓값, 최소값
print(min([-8, 2, 7, 5, -3, 5, 0, 1])) # -8
print(max([-8, 2, 7, 5, -3, 5, 0, 1])) # 7

#소숫점 반올림
print(round(17 / 3, 4)) #소수점 둘째자리까지

#날짜 표시하기
import time
print(time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time())))

import random

lotto = []

while len(lotto) < 6:
    num = random.randint(1,46)
    if num not in lotto:
        lotto.append(num)
    print(lotto)


import random
import itertools

person = ['김승현','김진호','강춘자','이예준','김현주']
work = ['청소','빨래','설거지','휴식','휴식']

random.shuffle(person)
random.shuffle(work)

zip1 = list(zip(person,work))

print(zip1)

class Account : 
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_balance(self):
        return "{}님의 현재잔액{}원".format(self.name, self.price)
    
    def deposit(self,price):
        self.price += price
        print(price)

    def withdraw(self,price):
        if self.price < price :
            print('잔액부족')
        else :
            self.price -= price




acc1 = Account("홍길동", 10000)
acc1.show_balance() #-> 홍길동님의 현재 잔액 10000원
acc1.deposit(5000) #-> 현재 금액+5000 원 더하기
acc1.show_balance() #-> 홍길동님의 현재 잔액 10000원
acc1.withdraw(3000) #-> 현재 금액 - 3000
acc1.show_balance() #-> 홍길동님의 현재 잔액 10000원
acc1.withdraw(30000) # 잔액 부족
acc1.show_balance() #-> 홍길동님의 현재 잔액 {}원