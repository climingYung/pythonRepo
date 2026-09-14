#예외처리
#SyntaxError, NameError, Index, ZeroDivision, Key, value, type Error 종류

#print('hi')

#x = 3
#y = 4
#print()
#print(4/0)

#a= {"a" :"gg", "b":33}
#print(a['c'])

#x = [1,2,3]
#x.remove(2) 
#x.remove(5) #value(에러)


# li = ['db', 'python', 'react']
# try: #예외가 날 수도 있는 코드블럭
#     x = 'java'
#     y = li.index(x) #예외발생 하자마자 except로 넘김
#     print('try블럭 수행')
# except ValueError: #예외 발생하자마 전달
#     print('except 블럭 수행')

# else : #예외 없을 떄 실행되는 블럭
#     print('else')


# li = ['db', 'python', 'react']
# try: #예외가 날 수도 있는 코드블럭
#     x = 'java'
#     y = li.index(x) #예외발생 하자마자 except로 넘김
#     print('try블럭 수행')
# except Exception as e : #예외 발생하자마 전달
#     print(e) #java is not in list 

# else : #예외 없을 떄 실행되는 블럭
#     print('else')

# class MyError(Exception) :
#     def __str__(self): # except에서의 e를 정의하는 특수 메소드
#         return "허용되지 않는 별명입니다."
# def say_nick(nick):
#     if nick == '바보':
#         raise MyError() #바로 except절로 넘어감
#         print(nick)
# try : 
#     say_nick("천사")
#     say_nick("바보")
# except MyError as e:
#     print(e)

#__call__ 객체를 함수형태로 쓴다.
#클로저
#함수 안에 함수를 결과로 반환할때 (콜백, 데코레이터 함수에서 사용) (inner function)
#내부함수가 바깥 함수의 n1을 기억하고 사용할 수 있는 구조로 되어있다(클로저 특징)
def add(n1):
    def wrapper(n): # n1의 값을 기억하고 있음 
        return n1 + n
    return wrapper

a1 = add(10) # a1 = wrapper
print(a1(10)) # wrapper(10)
a2 = add(20)
print(a2(10))

# a1 = add(10) => n1 = 10 저장 -> wrapper함수를 리턴(반환) 받고 있음 ->  a1에는 wrapper가 들어감 
# print(a1(10)) => print(wrapper(10))


#336.p
#데코레이더 = 함수를 장식하는 도구 기능 확장에 유용
#함수에 @기능을 붙인다

#클로저 사용

# def trace(func) : # 매개변수에서 hi가 들어감
#     def wrapper():
#         print('시작')
#         func()
#         print('끝')
#     return wrapper #함수반환

# def hi():
#     print('hi')

# t1 = trace(hi) #hi가 매개변수 func trace에 값 전달
# t1() #wrapper를 호출함

# #클로저 사용해 데코레이터 기능구현
# def trace(func) : # 매개변수에서 hi가 들어감
#     def wrapper():
#         print('시작')
#         func()
#         print('끝')
#     return wrapper #함수반환

# @trace #trace trace("hi")
# def hi():
#     print('hi')

# @trace #trace("hello")
# def hello():
#     print('hello')

# hi() # hi = trace('hi) wrapper를 리턴 받음
# hello()

#kwargs = 반환값은 딕셔너리
def trace(func) :
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) #big 함수값이 result에 저장
        print(args, kwargs, result)
        return result
    return wrapper


@trace #wrapper = trace(big)
def big(*args): # wrapper(10,20) 실행 -> result = max(10, 20) => 20반환
    return max(*args)
print(big(10, 20)) #20을 돌려받음 
#1. 데코레이터 호출되면 wrapper실행됨

@trace 
def mini(**kwargs):
    return min(kwargs.values())
print(mini(x=20, y=30, z=40))

#__call__ 메서드

class Tr :
    def __init__(self, func): #2번째 실행 hi함수가  
        self.func = func # hi()함수  저장 => hi는 Tr 클래스에 인스턴스가 됨  -> 그 이후 hi를 호출하면 함수가 아니고 인스턴스 이므로 파이썬 내부에서 __call__을 자동호출함 
        #-> __call__ 안에서 self.func.__name__ => hi를 출력 -> self.func()로 원래 hi함수를 실행하고 다시 이름(hi) 출략
    def __call__(self): 
        print(self.func.__name__, "시작")
        self.func()
        print(self.func.__name__, "끝")

#클래스형 데코레이터 :
#@데코레이터 : 함수 , 인스턴스로 바꿔주는 문법
#hi2 = Tr(hi) #객체명 = 클래스 객체 생성 코드

@Tr #Tr 클래스의 __init__에 hi를 전달해줘 -> func값이 hi가 되면서 hi는 함수가 아니라 Tr의 인스턴스
def hi():
    print('hi')
hi()#는 현재 인스턴스가 되어있음 인스턴스 함수처럼 사용했기 떄문에 __call__ 자동 호출됨

class MyError(Exception):
    def __str__(self):
        return "허용되지 않은 연산"


def calc(op, *arg):
    try:
        if op == 'add':
            return sum(arg)
        elif op == 'mul':
            result = 1
            for i in arg:
                result *= i
            return result
        elif op == 'avg':
            result = sum(arg) / len(arg)
            return round(result)
        else:
            raise MyError()
    except MyError as e:
        print(e)


print(calc("add", 1, 2, 3)) # 6
print(calc("mul", 1, 2, 3, 4)) # 24
print(calc("avg", 10, 20, 30)) # 20
print(calc("avg3", 10, 20, 30)) # None # 예외 avg3을 찾지 못함

# 사용자 정의 예외(예외를 만듬)


class MyError(Exception):
    def __str__(self):
        return "입력이 정확하지 않습니다"
    # def __init__(self): # init__에 값이 들어감
    #         super().__init__("0보다 커야해") 
try : 
    age = int(input('나이를 입력해주세요'))
    if age <=0:
        raise MyError() #생성자 함수 
    elif age <= 18 :
        print('미자는 꺼지고')
    else:
        print("입력완료")
except Exception as e:
    print(e)