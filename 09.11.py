class Car:
    #205.p
    def __init__(self,make,model,year): #특수 메소드
        self.make = make #인스턴스 변수
        self.model = model #인스턴스 변수
        self.year = year #인스턴스 변수
        self.speed = 0 #Car객체의 속성 speed를 선언하여 초기화


    #인스턴스메소드는 첫번째 인자로 항상 self가 있어야함
    def name(self):
        name = str(self.year) + " "+ self.make + " " + self.model
        return name
    
    def speed1(self):
        print(str(self.speed) + "이다")


#객채명 = 클래스명(init함수의 매개변수)
#객체생성코드 -> 자동으로 _init_ 호출
c1 = Car('tesla','modelS', 2018)
c1.name() #인스턴스를 통해 호출하면 파이썬이 자동으로 인스턴스를 Self에 넣어줌
c1.speed1()


#object 클래스 상속 207.p
class Fruit : 
    price = 20000 #클래스 자체의 변수 

    def __init__(self, title, color):
        self.title = title
        self.color = color
    def info(self):
        return "{}과일은 {}색".format(self.title, self.color)
    
    def buy1(self,buy1):
        return"{}과일은 {}에서 사야지".format(self.title, buy1)

#객체 인스턴스 생성
f = Fruit('pineApple' , 'yellow')
f.info()
f.buy1('청량리')

f2 = Fruit('apple' , 'red')
f2.info()
f2.buy1('신세계')

class A:
    def add(a,b): #클래스 메서드(정적메소드)로 보고 코드를 구현하겠다(self 지정 X)
        print(a + b)

    def minus(a,b): #동일
        print(a - b)
#객체생성코드
class A:
    def add(a,b): #클래스 메서드(정적메소드)로 보고 코드를 구현하겠다(self 지정 X)
        print(a + b)

    def minus(a,b): #동일
        print(a - b)
#객체생성코드
#a = A()
#a.add(3,4) a라는 인스턴스를 받을 self가 없음
#a.add(3,4)

#객체로부터 클래스메소드에 접근 불가
#클래스명으로부터는 가능
A.add(3, 4)
A.minus(5, 3)
#1
class Calculator : 
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class upgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = upgradeCalculator()
print(cal.add(10))
print(cal.minus(7))
print(cal.value)

#2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)


#3
one_list = [1,2,3,4]
result = list(map(lambda x : x * 3, one_list))
print(result)

class Container :
    stock_num = 0 #클래스 변수 => 모든 객체가 공유가능 -> 클래스명.변수

    def __init__(self,name):
        self.name = name
        Container.stock_num += 1

c = Container('Lee') #self.name = "Lee" 객체생성하면서 stock_num = 1
c2 = Container('Kim') #stock_num = 2
print(Container.stock_num)
print(c.__dict__)
print(c)

#내장 함수(자주 사용하는 함수)

print(abs(-3))

#all(),any() :iterable 요소 검사 (참, 거짓)

print(all([1, 2, 3])) #True
print(all([1, 2, 0])) #False

print(any([1, 2, 0])) #or(하나라도 참인 요소있으면 True)

new_list = [50, 1, 4, 10, 50]
if all(i < 20 for i in new_list): #20보다 큰 값이 모두 있어야 True
        print("ok")
else :
    print("cancel")

new_list = [50, 1, 4, 10, 50]
if any(i < 30 for i in new_list): #30보다 큰 값이 하나라도 있으면 True
        print("ok")
else :
    print("cancel")

#chr : 아스키 - > 문자, ord:문자 -> 아스키

print(chr(65))
print(ord('A'))

#enumerate() : 인엑스 + 
for i, name in enumerate(['body','foo','bar']):
    print(i, name)

#filter() : 반복가능한 객체 요소를 지정한 후 조건에 맞는 값 추출
def num(x):
    return abs(x) > 3

print(list(filter(num, [-3, 2, 4, -4, -10, -100])))

#람다식
print(list(filter(lambda x : abs(x) > 3, [-3, 2, 4, -4, -10, -100]))) 

#250p
#map() : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
#반복가능한 객체 : 리스트, 튜플, 문자열, 딕셔너리, range, 파일객체

def num2(x):
    return x * 3

print(list(map(num2 , [-3, 2, 4, -4, -10, -100])))
print(list(map(lambda x : x * 4, [-3, 2, 4, -4, -10, -100])))

#range : 반복가능한 객체 반환
print(range(5)) #끝 숫자만 지정 0부터 4

print(range(1, 10, 2))

print(list(range(1,10,2)))

print(list(range(0, -10, -1)))

for i in range(0, -10, -1):
    print(i)

#p.251 max, min : 최대,최소
#반복가능한 요소가 오면 된다 튜플 딕셔러니 문자열 range
print(max([1,2,3]))
print(max("python"))

print(min([1,2,3]))
print(min('python'))

#round() :반올림

print(round(4.6))
print(round(3.6432,2)) #소수점 둘째자리까지

#sorted : 반복가능한 객체 정렬 후 반환
print(sorted([5,6,1,2,5,6,7,8]))
a = sorted([5,6,1,2,4,5,6,1,3])
print(a)
print(sorted(['c','r','e','e','d']))

#sum() : 반복가능한 객체 합 반환
print(sum([1,2,3,4,5]))
print(sum(range(101)))

#type : 자료형 반환
print(type(3)) #int
print(type({})) #dict : 딕셔너리
print(type(())) #tuple : 튜플
print(type([])) #list : 리스트

#255.p zip
#반복가능한 객체의 요소를 묶어서 반환(인덱스 순서대로)
print(list(zip([10,20,30],[40,50,60]))) #타입은 리스트
print(list(zip([10,20,30],[40,50,60],[70,80,90])))#타입은 리스트
print(list(zip("abc","def")))#타입은 리스트

#257~258.p
#time : 시간관련처리
#import time 
import time
print(time.time())
print(time.localtime(time.time()))
print(time.ctime())

#포멧코드(형식 표현)
print(time.strftime('%Y %m-%d %H:%M:%s', time.localtime(time.time())))

#263.p
#random -> 랜덤 함수 추출
import random
print(random.random())
print(random.randint(1, 10)) #10도 포함


#섞기 shuffle()
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

#무작위 선택 choice()
c = random.choice(d)
print(c)

#273.p pickle()
#pickle : 객체 파일 쓰기 **
import pickle
f = open('test.obj','wb') #파일을 쓰기용 바이너리 모드로 열기
obj = {1 : 'python', 2 : 'study', 3:'basic'}
pickle.dump(obj,f) #객체를 파일에 저장
f.close()

with open('test.obj','rb') as f:
    data = pickle.load(f) #객체를 파일에 저장
    print(data)

f = open('test.obj','rb') #파일을 쓰기용 바이너리 모드로 열기
data = pickle.load(f) #객체를 파일에 저장
print(data)
f.close()

#286.p
import webbrowser
webbrowser.open('https://wikidocs.net/192016')
webbrowser.open('https://www.shinsegaev.com/event/initEventDetail.siv?event_no=E260815621&partnerNm=SVGS3020&utm_source=google&utm_medium=cpc&utm_campaign=siv_all_br_SVFK0106&utm_content=2609_sales_SVGS3020&utm_term=sivillage&gad_source=1&gad_campaignid=19751035088&gbraid=0AAAAADPEt-AYdI-CVf-pLn1W9btMAFVJ4&gclid=Cj0KCQjwzY7VBhDwARIsAFtPvBQLsLffEiVR4sNnzd5nXexQENflpinpUSdmVuPP8zsZElWLgypTx9waAm9WEALw_wcB')

#213.p
#모듈 : 파이썬 코드 들어있는 파일(.py파일 하나)
#패키지 : 여러 모듈을 폴더로 묶은 것
#라이브러리 : 여러 패키지, 모듈을 모아놓은 것(ex. pandas, numpy)

import test

