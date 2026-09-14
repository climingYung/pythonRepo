# pin = "881120-1068234"
# yyyymmdd = pin[0:6]
# num = pin[7:]
# print(yyyymmdd)
# print(num)
# print(pin[7])
# #format - c스타일(%s: 문자열, %f: 실수, $d:정수)
# print('문자열 %s와 문자열 %s가 있다' %('one', 'two'))
# print("%d %d" %(3,4))
# print("%f" %(3.14))
print("%10s" % "hi")#10자리 공간안에서 오른쪽 정렬로 hi출력 len()10

sosu = 3.42134234
print(len("%10.4f" % 3.42134234))

#format()함수 뒤에는 name=value 같은 형태로 입력값이 있어야함 
#:> 오른쪽 정렬 :< 왼쪽 정렬 :^ 가운데 정렬 
# : >정렬 사이에 지정한 문자 값으로 채워 넣을 수도 있다

print("%10s" % ("python")) #10의 자리에서 오른쪽 정렬로 
print("{:>10}".format('python')) #10자리에서 오른쪽 정렬로
print('%-10s' % ("python"))
#5자리까지 절삭
print('%.5s' % ("pythonJavascript"))

print("%6.2f" % (3.141592112345667)) #총 6개에서 소수점은 2자리 "%06.2f" /앞부분의 공백은 0으로 채워줘


x = 30
y = 50
z = 42032
str = "Kim"

ex1 = '%s %f %d' %(str, z, (x+y))
print(ex1)
print(type(z))

print("{0:<10}".format('hi')) #왼쪽 정렬
print("{0:^10}".format('hi')) #가운데 정렬
print("{0:>10}".format('hi')) #오른쪽 정렬


#"script 오른쪽 정렬" %는 서식 문자 0은 생략가능
scr = "script"
print("{0:>20}".format(scr))
print("%20s" %(scr))

#"script" 왼쪽 정렬
print("{0:<10}".format(scr))
print("%-10s" %(scr))

#10자리로 왼쪽 정렬하는데 나머지 자리는 _로 채운다
test = "Python"
print("{:_<10}".format(test))

#10자리로 가운데 정렬(<, >, ^와 숫자사이에 공백채우기(지정한 문자값))
print("{:^10}".format(test))

name = "홍길동"
age = 30
#f 문자열 포매팅은  변수값을 생성한 후에 그 값을 참조할 수 있다
f'나의 이름은 {name}입니다 나이는 {age}입니다'
#f 문자열 포매팅 연산자를 쓸 수 있다
f'나의 이름은 {name}입니다 나이는 {age+5}입니다'

#기존에 .format을 쓰던 방식 위에랑 같은 표현
name2 = "홍길동"
age2 = 30
str2 = '내 이름은 {0}입니다. 나이는 {1} 입니다.'.format(name2, age2)
#0,1은 자바스크립트 함수에서의 매개변수 느낌
############################################################
x = 10
y = 30
z = "Lee"
#c스타일(서식문자)
test1 = 'z=%s, sum=%d' %(z, (x+y))
print(test1)

#포매팅 방식
test2 = 'z={z}, sum={sum}'.format(z=z, sum = x + y)
print(test2)

#f문자열 포매팅 방식
test3 = f'z={z}, sum={x+y}'
print(test3)

#정렬 hello 오른쪽 정렬로 10자리 주면서 출력
print(f"{'hello':>10}")
print(f"{'hello':^10}")

#변수에 담긴 거 정렬
print(f'{name2:>10}')

#n을 왼쪽 정렬 20개의 자리수 채우면서
n = 50
print(f"{n :<20}")

#3시30분부터
#n을 왼쪽 정렬 10개의 자리수 채우면서 공백을 -으로 채우기
print(f"{n :-<10}")
#n을 오른쪽 정렬 20개의 자리수 채우면서 공백을 #으로 채우기
print(f"{n :뛻>20}")

#파이썬 리스트
#파이썬에서는 배열 제공하지 않는다
#리스트 (순서 o, 중복 o, 수정 o, 삭제o)

#p.77
list1= []#빈 리스트 참조) 자바스크립트의 배열과 유사하지만 좀 다름

list2=list() #빈 리스트
print(type(list1), type(list2)) ##리스트 객체

list3 = [60,100,98,95]
list4 = [60,1000,"딥티크","바이레도"] #문자열,정수를 섞어서 리스트정의가능
list5 = [60,10000,['Tom','딥티크','jack']] #리스트안에 리스트를 정의가능
list6 = [3.42,'python',3,14,False,3.2212] #bool타입도 리스트안에 정의가능

print(list4[1])
print(list4[0] + list4[1] + list4[1]);
print(list4[-1])
print(list5[-1][1]) #뒤에서 첫번째의 배열의 인덱스 1번값 딥티크

#슬라이싱
print(list4[0:3]) #0은 생략가능
print(list4[2:]) #인덱스2부터 끝까지(마지막 생략시)
print(list5[2][:3])

print([list3+list4]) # + 연사자를 사용하면 리스트끼리 나열됨 차레대로
print([list3 * 3]) # *반복 개념 list3 * 3 리스트를 3번 반복함
#int와 str은 더하기가 안됨 str()로 명시적으로 바꿔줄 수 있음
print(str(list3[0]) + "hi")

#수정
list4[0] = 4
print(list4)
list3[1:2] = ['a', 'b', 'c'] ##인덱스1번부터 2미만 까지 값 변경 대괄호(리스트 안에 넣을 값의 형태) 2개면 리스트를 리스트안에 넣겠다 
print(list3)

del list3[3] 
print(list3)

name = '에릭'
print("안녕 %s 좋은아침이네" %(name))
print("안녕 {0} 좋은아침이네".format(name))
print(f"안녕{name} 좋은아침이네")

x = 3 
y = 5

print("X = %d , Y = %d" %(x,y))

print("x = {0}, y = {1}".format(x,y)) #.format에서 0,1 안적어도 순서대로 나옴

print(f"x = {x}, y = {y}")


a = [5,3,2,4,1]
han = ['ㄷ','ㅇ','ㄹ']
a.append(6) #리스트 맨 마지막에 추가

a.sort() #오름차순 정렬 #알파벳이면 알파벳 순서정렬
han.sort()
print(han) #한글도 ㄱㄴㄷ순서로 정렬
print(a)
a.reverse()
print(a) #거꾸로 출력

print(a.index(5)) #5의 위치
a.insert(2,7) #인엑스 3번위치에 7삽입
print(a)

a.reverse() #원본 유지가 안됨
print(a)

a.remove(1) #중복의 경우 첫 번째의 나온 값만 삭제된다.
print(a)

print(a.count(4))
ex1 = [8,9]
a.extend(ex1)
print(a)

#리스트 선언
li1=[]
li2=list()
li3=[4,2,6,7,1]
li4=[3,3,'jack','tom']
li5=[1,3,['banana','apple','orange']]
li6=[2,True,False,'mango','coffee',3.43]

#li4 tom출력
print(li4[3])
print(li5[2][1])
li4.reverse() # = ::-1
print(li4)
a = "abcdefg"
print(a[0:5:2]) #리스트명[초기인데스 : 끝인덱스 : 증감]

letters = ['a', 'b', 'c', 'd', 'e']
items = ['zero', 'one', 'two', 'three', 'four', 'five']

print(letters[1:4])
print(items[0::2])

invite = ['찰스','스누피','루피']
invite.insert(0,'둘리')
print(invite)
invite.append('토심이')
print(invite)
invite.pop() 
invite.pop()
invite.pop()
print(invite)

#튜플
#리스트처럼 순서가 유지가 됨 
#순서 O , 중복 O , 수정/삭제 X(sort, reverse, remove, pop)
#튜플 더하기, 튜플 곱하기는 가능
t1 = ()
t2 = (1,) #요소값이 하나라면 무조건 ,로 끝내줘야함
t3 = 1,2,3 #()소괄호 생략한거
t4 = (1,2,3) 
t5 = ('a', 'b',('ab', 'cd')) #리스트안에 리스트처럼 튜플안에 튜플도 가능하다

