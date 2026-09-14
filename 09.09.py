#141.p
#기초적인 for
test_list = ['one','two','three'] #리스트, 튜플, 문자열 사용가능
for i in test_list: #one two three를 순서대로 i에 대입
    print(i)

#while문과 비교
i = 0
while i < 2:
    print(test_list[i])
    i+=1

#튜플에서의 for문
a = [(1, 2), (3, 4), (5, 6)]
for(first, last) in a: #first에 1 last에 2 이런식으로 대입됨
    print(first + last) #마지막 더한 값 출력

names = ['KIM','LEE','JOO','JUNG']
for i in names:
    print(i) #리스트의 안에 값들이 i에 들어감

#문자열에서 for문 쓰기
word = "python"
for i in word:
    print(i) #순차적으로 한 글자씩 출력된다

profile = {
    "name" : "hong",
    "age"  : 13
}
for i in profile:
    print(profile[i],i) #딕셔너리에서 i는 키값 변수명[i]를 하면 안에 있는 값이 나옴

print("==============================")



#143.p
marks =  [90, 25, 67, 45, 80]
number = 0

for mark in marks :
    number = number + 1
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다")
    else :
        print(f"{number}번 학생은 불합격입니다")

fruit = "PineApple"
for i in fruit:
    if i.isupper(): #isupper()대문자인지 확인
        print(i)
    else :
        print(i.upper()) #upper()는 대문자로 바꿔줌

number_list = [12,125,1261,717,35,1771]
for i in number_list:
    if i == 35:
        print("35!")
        break #반복문 출력 35가 되는 순간 탈출
    else:
        print(i)
#144.p continue
marks =  [90, 25, 67, 45, 80]
number = 0

for mark in marks :
    number = number + 1
    if mark < 60:
        continue
print(f"{number}번 축하합니다 학생은 합격입니다")


#is : 두 객체가 같은 타입의 객체(메모리 주소가 같은지) 읹지 비교하는 연산자
# == : 값이 같은지비교
#type : 하나의 고정된 타입 객체 반환

li = ["3", 1, 2, True, 4.5]

for i in li :
    if type(i) is str: 
        continue #제외함
    print(i, type(i))


#for else 구문 
#else블록은 for문이 break로 중간에 끊기지 않고 끝까지 실행되었을때만 실행됨
number_list = [12,125,1261,717,35,1771]
for i in number_list:
    if i == 35:
        print("35!")
        break 
else : #else에 위치가 if블럭이 아니라 for랑 짝궁
        print("hihi")
#for else를 사용하는 이유는 for문이 다 돌고 실행 시켜야될 작업사용시 사용

fruit2 = "Mango"
print(reversed(fruit2)) #객체주소값
print(list(reversed(fruit2))) #리스트로 바꾸고 반대로 출력
#객체 안에 있는 값을 꺼내서 리스트로 만들어줌

print(tuple(fruit2))
print(set(fruit2))#집합은 순서가 뒤죽박죽

#144.p range()
for i1 in range(10): #0 ~10 미만
    print(i1)

#1~10
for i2 in range(1, 11):
    print(i2)

#while문 바꾸기
i = 1
while (i <= 10):
    print(i) #출력한 다음
    i += 1 # 더하기

for i3 in range(1, 11, 2) : #1 ~ 10 수 증 2씩 증가라는 뜻
    print(i3, end=" ") #end 일렬로 출력 공백으로

#p.145참고
#1부터 10까지 합
sum = 0
for i in range(1, 11) :
    sum = sum + i #i4 = i4 + 1
print(sum)


marks =  [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print(f"{number}번 축하합니다 학생은 합격입니다")

sum = 0
for i in range(1, 101) :
    sum = sum + i #i4 = i4 + 1
print(sum)

for i in range(2, 10) : # 2 ~ 9
    for j in range(1, 10): # 1 ~ 9
        print(i * j, end=" ")
    print(" ") #단 출력 후 줄바꿈

#카페문제풀이 8,9,10

# 8. msg="It is Time" 설정하고 for문 range함수를 사용하여 문자열 길이까지 다 출력 대문자인것만 뽑아서 출력
msg = "It is Time"
for i in range(len(msg)) :
        print(msg[i])
            
#강사님이 적은 답
msg = "It is Time"
for i in range(len(msg)) :
        print(msg[i])

for i in msg :
        if i.isupper():
            print(i)

#9. 1~10까지 수 중 홀수만 출력 (range, continue사용)
for i in range(1, 11):
    if(i % 2 == 0):
        continue
    else :
        print(i)

#10. 3~32까지 수 중 3의 배수만 출력
for i in range(3, 33) :
    if(i%3 == 0):
        print(i)


#147.p
a = [1,2,3,4]
result = [num*3 for num in a] #list 컴프리헨션 리스트안에 for
#풀이 : 위에 수식기준 num이 앞에 수식으로 num * 3
print(result)

a = [1,2,3,4]
result = [num*3 for num in a if num%2 == 0] #list 컴프리헨션 리스트안에 for
#if문도 가능 
#풀이 : for을 먼저 봐야한다 
print(result) #리스트형태로 나온다 why? 초반에 result라는 변수는 리스트 [ ]

a = [1,2,3,4]
result = [num for num in a] 
#for문을 먼저 작성한다
print(result)

test = [1,2,3,4]
for num in test:
    print(list(num))
#이건 오류가 나온다 int객체는 list로 만 들 수 없다
#why?직역하면 풀어진 값은 int인데 이 int를 리스트형태로 만들 수 없음
#그래서 빈 리스트에 append()를 사용해야함

#설명 result = [변수 for 변수 in collection]

#3~30출력
for i in range(3, 31):
    print(i, end =" ")

list_1 = [i for i in range(3, 31)] #리스트 컴프리헨션 방식
print(list_1)

list_1 = [i for i in range(3, 31) if i%3 == 0] #리스트 컴프리헨션 방식에서 if문 추가해서 3의 배수만 
print(list_1)

#1부터 10까지 -list
print([i for i in range(1,11)])

#148p
result = [x * y for x in range(2, 10)
                for y in range(1,10)]
print(result)


#149 ~ 151

#Q2
result = 0
i = 1
while i <= 1000:
    if(i%3 == 0):
        result +=i
    i += 1
print(result)

#Q3
i = 0
while True:
    i += 1
    if(i > 5):
        break
    print(i * "*")

#Q4
for i in range(1, 101):
    print(i,end = " ")

#Q5평균점수 구하기

A = [70,60,55,75,95,90,80,80,85,100]
total = 0 
for score in A:
    total += score
average = total / len(A)
print(average)

#q6리스트 컴프리헨션

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers :
    if n % 2 == 0 :
        result.append(n * 2)
print(result)

print([n* 2 for n in numbers if n % 2 == 1 ])

#함수 153.p
#개발자가 함수명 통해서 정의한 후 필요할 때마다 호출
#반복되는 코드를 한번 구현 한 후 재사용 가능하도록 만든 코드의 집합
#함수구현 후 - > 재사용

#매개변수가 있는 함수 
#매개변수가 없는 함수
#결과값만 반환하는 함수(return)
#결과값 반환 안하는 함수

def func1():
    print("함수1")
func1()

def fun2(a,b):
    print(a,b)
fun2(4,7)


def fun3(a,b):
    print(a +b)
fun2(10,32)

def name(word):
    print(word)
a = "python"
name(a)

def name2(word):
    n ='Hi' + (word)
    return n
print(name2("goooood"))

def multi(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return y1, y2, y3 #y1, y2, y3값을 리턴함
a,b,c = multi(10) #언패킹 작업 a = 50, b = 100, c = 200
print(a,b,c) #출력 50 100 200

def func1(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return (y1, y2, y3) #튜플 한덩어리로 묶어서 리턴함

a = func1(5)
print(a, type(a)) #a는 튜플
print(list(a)) #리스트로 형변환 후 출력


##################################

def func2(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return [y1, y2, y3]

b = func2(5)
print(b, type(b))

def func3(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return {"y1" : y1, "y2" : y2, "y3" : y3}

b=func3(5)
print(b)

#p.96 ~ 100p (딕셔너리로 반환 받았으므로 사용가능)
#y2의 대응값 출력
print(b.get('y2'))

#키, 값 다 출력
print(b.items())

#키만 출력
print(b.keys())

def qq(x,y):
    for i in range(x ,y):
            print(i , end = " ")
qq(1,10) #1~9까지 출력하는 함수
qq(4,6) #4~5까지 출력하는 함수


#p.160
#입력하는 값이 몇개가 될지 모를 때는 어떻게 해야해?
# 함수에 들어가는 매개변수 앞에 *을 붙여준다 예시 참고

def add_many(*args): #*매개변수
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

#p.161
#*을 붙인 매개변수 , 다른 매개변수도 쓸 수 있다
def func1(*args): #매개변수에는 튜플 리스트 문자열도 올 수 있다.
    for i in args:
        print(i)
func1('gildong')
func1('gildong','tom','juil')
func1('gildong','tom','juil','jack')

#p.162 keyword arguments
#**을 붙인 매개변수, 키워드 매개변수 kwargs
#def print_kwargs(**kwargs): 참고

def func2(**kwargs): #**로 딕셔너리 형태로
    for i in kwargs.keys():
        print(i, kwargs[i], type(i), kwargs)
#i는 key값 kwargs[i]는 밸류값 출력, type은 딕셔너리, kwargs는 **로 키워드매개변수므로 딕셔너리가 전체 나옴
func2(name1 = '철수')
func2(name1 = '페이커', name2 = '쵸비', name3 = '제카') # key : value 형태로 저장하겠다
func2(name1 = '겐지', name2 = '아나')

# *args : 반환은 tuple(튜플)
# **kwargs : 반환은 dict(딕셔너리)

def func3(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, *args, **kwargs)

func3(10,40, 'kim','lee','park', age=10, adr='seoul')
#arg1,arg2 => 10,40
#*arg3 => kim lee park
#**kwargs => age=10, adr='seoul' 무조건 맨 뒤에만 올 수 있다
#순서규칙 => 일반 인자 , *args, **kwargs 

#163.p
#함수의 리턴값은 언제나 하나이다


def calcu(name, time, count, price ):
    if(time == 15 and count >= 3):
        price = price * 0.9
        print("{}씨는 10%할인 = {}원".format(name,price))
        print("%s씨는 10%%할인 = %d원" %(name,price))
        print(f"{name}씨는 20%할인 = {price}원")
    elif time == 12 and count >= 5 :
        price = price * 0.8
        print("{}씨는 20%할인 = {}원".format(name,price))
        print("%s씨는 20%%할인 = %d원" %(name,price)) #%%을 두개쓴 이유는 %을 문자열 포맷팅으로 인식해버려서 오류가 나기 때문에
        print(f"{name}씨는 20%할인 = {price}원")
    else:
        print(f"{name}씨는 할인안됨 = {price}원")



calcu("형민",15,4,20000)
calcu("종진",12,5,50000)
calcu("한빈",10,2,70000)

#p.185
#Q1홀수, 짝수 판별하기
def is_odd(number):
    if number%2 == 1:
        return True
    else:
        return False

is_odd(9125126)
#Q2 모든 입력의 평균값

def avg_numbers(*number):
    result = 0
    for i in number:
        result += i
    return result/len(number)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

#165.p ~ 
#매개변수에 초깃값을 미리 설정가능함
#초기값은 무조건 맨뒤에 파이썬에서 판단이 어려운경우 읽지 못함

#초기값 설정
def say(name, man, old=20): #초기값은 무조건 맨뒤에 와야됨
    print(name)
    if man : 
        print('남자', old)
    else :
        print('여자', old)

say('juil',True) #인자로 old값으로 받은게 없어서 기본값인 20이 출력
say('Tom', False, 10) #10으로 인자를 전달해서 10출력


#171.p
#input은 사용자가 적은 걸 문자열로 저장함
#실수로 바꾸기 위해서 float()
a = input('너는 뭘 좋아하냐?')
print(a)

#how_height = input('키가 몇 cm야??')

#186.p
input1 = input("첫 번째 숫자를 입력하세요")
input2 = input("첫 번째 숫자를 입력하세요")

total = input1 + input2
print(f"두수의 합은 {int(total)}입니다")

#카페 문제 1, 2
#1. 키를 실수로 입력받아 "너의 키는 ( ) cm이다" 라는 문자열을 출력 format함수와 f-string사용
how_height = int(input('키가 몇이에요?'))
print(f"너의 키는({how_height}cm이다)")
print("너의 키는({}cm이다)".format(how_height))



#2. avg- 평균구하는 함수 구현해라. avg(1,2) avg(1,2,3,4,5) 호출코드이다.
def avg(*args):
    total = 0
    for i in args:
        total += i
    return total/len(args)
avg(1,2)
avg(1,2,3,4,5)

    