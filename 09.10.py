#167.p
#함수 안에서 선언한 변수의 효력범위

#함수 안에서 정의한 변수는 함수안에서만 사용가능
#자바스크립트의 함수안에서의 지역변수 개념이랑 비슷한거 같다

a = 1 #전역에서 생성한 변수
def vartest(a) :
    a = a + 1 
print(vartest(a)) # #vartest에 a를 대입 했지만 출력값 none
print(a) # 출력값 1

#함수 안에서 함수 밖으로 변수를 변경하는 방법

a = 1 #전역에서 생성한 변수
def vartest(a) :
    a = a + 1 
    return a 
a = vartest(3) # 
print(a) # 출력값 1

#1. vartest(3) 4 = 3+1 -> return 4 => a = 4 
#기존 전역에서 생성한 a는 1 이였지만 a = 4로 재정의

#169.p
#global을 사용하면 함수 안에서의 변수를 직접사용하겠다는 뜻
#하지만 함수는 독립적으로 사용하는것이 좋기때문에 권장 X

#170.p lambda 예약어(중요!!!!!!!!!!!!)
#함수_이름 = lambda 매개변수 : 실행문
#def를 사용해야 할 정도로 복잡도가 떨어지거나, def를 사용할 수 없는 곳에서 쓰임


#예시
add = lambda a, b: a + b
result = add(3, 4)
print(result)

#lambda로 바꾸기

def multi (x, y):
    return x * y

multi = lambda x, y: x * y
result = multi(3,4)
print(result)

def plus(x) :
    return x * 10
print(plus(1))

plus = lambda x : x * 10
result = plus(1)
print(result)

a = multi #함수명을 a 할당함(a는 별칭)
print(a(4,5))

def final(x, y, func1) : #함수를 다른 함수의 매개변수로 넘길 수 있음 
#==> 고차함수 -> multi가 final의 매개변수로 들어감
    print(x, y,func1(5,6)) #func1은 위에서짠 multi가 됨 
#자바스크립트의 콜백함수 구조랑 비슷함

final(1, 2, multi)


#171.p
#사용자 입출력
#리마인드 인풋은 입력값은 항상 String 즉 문자열로 들어온다

name = input('이름은?')
score = input('학점은?')
age = input('나이는?')

print(name, score, age)
print(type(name), type(score), type(age))
#input의 모든 타입은 String


#int() 
num1 = int(input('첫번째 정수')) #문자열 - > 정수타입으로 바꿔준다.
num2 = int(input('두번째 정수'))
print(num1 + num2)

#float() 실수 입력
float1 = float(input('실수입력'))
print(float1, type(float))

a, b = input('숫자입력').split() #p.76
#-> 공백을 기준으로 문자열을 나눔
a = int(a) 
b = int(b)
print(a + b, type(a+b))

dict = {}

while True : #무한 반복
    name = input('이름은?')
    tv = input('tv좋아해?')
    dict[name] = tv

    ans = input('친구한테도 물어볼까?')
    if ans == 'no':
        break
    print(dict.items())

####################3개다 같은 출력인데 이렇게도 사용가능하다##########
li = [i for i in range(1,6)] 
print(li)

li2 = list(range(1,6)) #리스트로 1부터 5까지 출력
print(li2)

re = list()
for i in li2:
    re.append(i) #빈 리스트에 1,2,3,4,5를 넣겠다
print(re)
####################################################################


#242.P 
#abs() 어떤 숫자를 입력받았을 때 그 숫자의 절댓값을 리턴하는 함수

print(abs(3))
print(abs(-3))
print(abs(-1.2))

#all()
#()안에 들어온 데이터가 모두 참이면 True, 하나라도 True가 아니면 False
#빈값도 True로 반환

#any()
#안에 들어온 데이터가 하나라도 참이면 True, 모두가 거짓일때만 False

#chr()
#유니코드를 숫자값으로 받아 그 코드에 해당하는 문자를 리턴

#244.p
#enumerate() 중요

#245.p
#filter() 중요
def positive(x) : # 여기서 x는 [1, -3, 2, 0, -5, 6] 이 리스트
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
#positive는 함수
#list 구조
#for if문 기능이 합쳐진 느낌

#250.p
#함수와 반복 가능한 데이터를 입력으로 받음
#map()은 입력받은 데이터의 각 요소에 함수를 적용한 결과를 리턴하는 함수
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result
result = two_times([1, 2, 3, 4])
print(result)


#map(f,iterable)
#map(함수, 반복가능한데이터), map은 if보단 반복문의 느낌
def two_times(x):
    return x * 2
list(map(two_times, [1, 2, 3, 4]))
#list형태로 map(함수(two_times),반복가능한 데이터([1, 2, 3, 4]))

def pp(x) :
    return x+20
print(pp(4))

print(list(map(pp, [1,2,3])))

def on(i):
    return i

#리스트의 요소를 하나씩 one의 매개변수로 받아 리턴한다.
re2 = list(map(on, [1,2,3,4,5]))
print(re)

#lambda식으로 표헌
one = list(map(lambda i:i, [1,2,3,4,5]))
print(one)

#map을 사용해 10씩 증가
list1 = [1,2,3,4,5]
re3 = list(map(lambda i:i+10, list1))
print(re3)

for i in re3:
    print(i)

#list comprehension
#map, filter는 lambda식이랑 같이 활용이 높다
#lambda def를 사용할정도로 함수의 길이가 짧을때 사용


#246.p
#3보다 작은값 list로 출력 람다식 이용
new_list = list(filter(lambda x : x < 3, range(1,6)))
print(new_list)

#1부터 10까지 list로 출력하는데 10씩 더해서 출력
new_list = list(map(lambda i : i+10, range(1,11)))
print(new_list)

def square(x):
    return  x**2

new_list1=[1,2,3,4,5]
re = list(map(square,new_list1))
print(re)

re2 = list(map(lambda x : x**2, new_list1))
print(re2)

re3 = [i**2 for i in new_list1]
print(re3)

#1부터 20까지의 수에서 2의 배수만

re4 = [i for i in range(1,21) if i%2 == 0]

re5 = list(filter(lambda i : i%2==0, range(1,21)))
print(re5)

#175.p ~ 179.p
#파일 읽고 쓰기
#읽기 : r 파일을 읽기만 할 때 사용
#쓰기 : w 파일에 내용을 쓸 때 사용
#추가 : a 파일의 마지막에 새로운 내용 추가시 사용
#인코딩 : 문자를 숫자로 바꾸는 것 
#디코딩 : 숫자를 문자로 바꾸는 것
#utf - 8 : 가장 많이 쓰는 국제 표준 인코딩(유니코드)


#f = open('파일명', 파일열기모드)

#1. read함수 사용
f = open('./resource/news.txt','r', encoding ='UTF-8')
print(f.encoding)
print(f.name)
print(f.mode)
result = f.read() #파일로 부터 읽어온다.
print(result)
f.close() #파일을 열었으면 반드시 다기

#2.파일객체를 for문과 사용
f = open('./resource/news.txt', 'r' , encoding ='UTF-8')
for i in f:
    print(i)
f.close()

#3. with
with open('./resource/news.txt', 'r' , encoding ='UTF-8') as f:
    c = f.read() #read()는 문자열
    print(type(c))
    print(list(c)) #싹다 list형태로 출력됨

print("======================================================")
with open('./resource/news.txt', 'r' , encoding ='UTF-8') as f:
    c = f.read(30)
    print(c)

#4.readline()
#첫번째 줄만 읽어서 출력함
with open('./resource/news.txt', 'r' , encoding ='UTF-8') as f:
    line = f.readline()

#5.readlines() 반환형이 리스트임
with open('./resource/news.txt', 'r' , encoding ='UTF-8') as f:
    lines = f.readlines()
    for i in lines:
        print(lines)

#6. w : 쓰기모드(파일생성)
with open('./resource/text1.txt', 'w') as f: #test1.txt파일을 생성하여
    f.write('hi python!!\n') #test1파일에 텍스트생성

#7. a : 덧붙이기 마지막에 추가
with open('./resource/text1.txt', 'a') as f: #test1.txt에 내용을 쓰겠다
    f.write("Hi React!!!")

with open('./resource/text1.txt', 'w') as f: #test1.txt에 내용을 쓰겠다
    li = ['React\n','DB\n',  'Python\n' ]
    f.writelines(li)

#p.190
#객체(object) : 파이썬에서 존재하는 모든 것
#               ex) 123, "hello",[1,2,3],Dog()(정수/실수, 문자열, 튜플,딕셔너리, 함수)
#class 설계도
#object 설계도를 바탕으로 실제 만들어진 제품

#클래스
#self, 인스턴스 메소드, 인스턴스 변수
#클래스 메소드, 클래스 변수

#객체(object) : 클래스의 인스턴스를 포함한 모든 파이썬 데이터
#/123, "hello", [1,2,3]
#인스턴스(instance) : 특징 클래스에 의해 생성된 객체를 지정할 때
#class로 부터 만들어지는 객체에는 제한이 없음 
#동일한 클래스로 만든 객체는 서로 아무 영향이 없음

#194.p
class Profile : # class class명
    pass # 패스 의미

p = Profile() #p는 Profile의 인스턴스. Profile은 설계도 
#위는 생성자

class class_test :
    def setdata(self,first, second):
        self.first = first
        self.second = second
#.205.p
class Profile :
    name = "gilbong" #클래스 변수(클래스 블록 안 - 모든 인스턴스 접근가능(공유))
    #인스턴스 변수 : 각 인스턴스 마다
    def __init__(self,name, age):
        self.name = name
        self.age = age
p = Profile("gildong",13)
p2 = Profile("jiji",23)

print(p == p2) #false
print(id(p), id(p2)) #서로 다른 주소값을 가진다

print('{0} {1} {2} {3}'.format(p.name,p.age,p2.name,p2.age))
#객체 이므로 .으로 객체안에 요소에 접근가능 

#112.p 114.p
c = p
print(p == c, id(p), id(c)) #같은 주소를 쓰고 값도 같음

from copy import copy
c=copy(p)
print(p == c, id(p), id(c))  #서로 다른 주소를 가지지만 값은 같음

#인스턴스 메소드, 인스턴스 변수
#클래스 메소드, 클래스 변수

class Test:
    def func1() :#self 인자가 없는 함수 -> 클래스 안에 있지만 인스턴스 메소드 아님
        print("Func1!!") #func1은 결룩 클래스안에 메소드로 들어감

    def func2(self): #인스턴스 메소드로 호출시 자동으로 self(인스턴스 객체 자신)가 전달됨
        print(id(self))
        print("Func2!")

t = Test()

#t.func1() #예외 -> func1()에는 self가 없는데, t.func1()호출시 파이썬 내부적으로 func1(t)를 호출하려고함

t.func2() 
Test.func1() #클래스에서 직접 호출
Test.func2() #예외 -> func2(self)인데 인자가 없이 호출해서 인스턴스가 없어서 예외
Test.func2(2) #직접 인스턴스 t를 self로 넘겨 호출
