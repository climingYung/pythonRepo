## str문자열
# list 리스트
# tuple 튜플
# set 집합
# dict 사전(딕셔너리)
#...

str1 = "python"
str2 = 'How are You?'

#type() 타입출력

str5 = ''
print(type(str5) , len(str2))

int1 = int(5.6) #5.6을 가지고 정수형 객체로 형 변환환

print(int1)

float = float(4) #4를 실수형 객채로 형변환

#P.52
ex_str1 = "Do you have a \"phone\"?" #""큰따옴표 버전
print(ex_str1)

ex_str2 = "Do you have a \'phone\'?" #''작은따옴표 버전
print(ex_str2)

#p.54(이스케이프 코뜨)
t_str1 = "Py \t thon"
print(t_str1)

t_str2 = "New \n Python"
print(t_str2)

#문자열 연산

str_1 = "Apple"
str_2 = "Banana"
str_3 = "Cherry"
str_4 = "Mango"

print(3*str_1) #*중복
print(str_1 + str_2) # +문자열 나열

print('p' in str_1) # 문자열 안에 p가 들어가 있는지 true/false 값으로 알려줌 (in)
print('c' in str_3)
print('A' in str_4)

#문자열 형변환 str()
print(type(str(33))) #33의 정수형 객체 -> 문자열객체로 바꿔서 데이터자료형 출력
print(str(3.4)) 
print(str(True))

#format 사용 (%d , %s, %f, %c)
print("%s %s" % ('first', 'second'))
print("{0} {1}".format('first', 'second'))

print("%10s" % ('Python')) #오른쪽 정령

#format
#p.69
print("{:>10}".format('python'))
print("%-10s" % ('Python'))
print("{:<10}".format('python'))


#10에 python * 포함(왼쪽 정렬)
print("{:*>10}".format('Python'))
#10에 python * 포함(중앙 정렬)
print("{:*^10}".format('Python'))

#절삭
print("%.3s" %('pythonjava')) #세글자만 출력하고 나머지 버림
print("{:3}".format('pythonjava'))
print("{:10.3}".format('pythonjava')) #10개의 자리를 주면서 3글자만 나오게

print("%d %d %d" %(2,3,4)) #C스타일의 제한 없음 정수라 %d

#4자리수에서 정수 12출력 (C스타일)
print("%4d" %(12)) #4자리수에서 정수 12출력

#4자리수에서 정수 12출력 (.format) (정렬이 없어서 < > ^ 사용X)
print("{:4}".format(12))

print("%f" % (1.22342333231123)) #6자리까지만 나오게 %f

#최소 3자리 공간을 확보해서 출력
#최대길이를 제한하는것이 아님
print('%3d' %(1.22342333231123))
print('%3s' %('pythonjava'))
print('%-3s' %('pythonjava'))

#p.66
print('%3s' %("py")) #최소 3자리 공백확보됨 (오른쪽 정렬)

print("%4.2f" % (3.2333333)) #4자리의 공간을 확하고 소숫점 두번 째자리까지만 출력
print("%5.2f" % (3.2333333)) #5자리의 공간을 확하고 소숫점 두번 째자리까지만


tu1 = ()
tu2 = (1, )
print(type(tu1))


#튜플
tu = (5,2,4,4,3)
print(tu.index(5)) #5의 위치 찾기
print(tu.count(4)) #4가 몇 개인지 찾기
#교재의 없는 부분 패킹, 언패킹
#packing(패킹) : 여러개의 값을 하나의 튜플, 딕셔너리, 리스트 등으로 묶는 작업
#Unpacking(패킹) : 튜플, 딕셔너리, 리스트로 묶여 있는 값을 개별(각각 변수)로 푸는 작업
tu22 = ('phone', 'book', 'computer', 'mouse') #packing

#Unpacking(패킹) 
(x,y,z,m) = tu22
print(x,y,z,m)
(x,y,z,m) = ('phone', 'book', 'computer', 'mouse')
#x , y, z, m의 각각 변수에 값을 대입시키는 방법(unpacking)
print(x,y,z,m)

tu33 = 1,2,3 #튜플 팩킹
tu44 = 4, #하나의 값이 있기 때문에 , 붙여줌 안 붙이면 튜플로 인식 못함

x1,x2,x4 = tu33
x4,x5,x6 = 4,5,6

print (x1,x2,x4)
print (x4,x5,x6)


#딕셔너리
#순서 유지 x , key중복x 유니크한 값 , 추가 O, 삭제x

#p.94
dic1 = {'name' : 'Lee' ,'phone' : '010-1234-5678', 'birth' : '000211'}
dic2 = {0 : 'python'} #key값은 정수형태로도 가능
dic3 = {'ary' : [1,2,3,4]} #key값의 value는 리스트형태
dic4 = {
    'name' : 'tom',
    'addr' : 'seoul',
    'age'  : '22',
    'grade' : 'A',
    'status' : True
} 
dic5 = dict() #{} 빈딕셔너리
dic6 = dict([('name','tom'),('addr','seoul'),('age','22'),('grade','A'),('status', True)])
# 가장 안쪽 구조 : 튜플 구조
# 안쪽을 감싸는 구조 : 리스트 구조(여러개의 튜플을 하나로 묶음 -> 튜플의 리스트)
# 가장 바깥쪽 구조 : 튜플의 리스트를  딕셔너리 구조로 변환해줘

#(,) 튜플의 구조 -> 튜플 들의 리스트 -> dict() -> 딕셔너리(키:값)
print(dic6)
#dict()객체는 인자를 하나밖에 받지 못함!!!(중요)

print(type(dic1),type(dic2),type(dic3),type(dic5),type(dic6))

#p.96
#key를 사용해서 value를 얻는 법
#딕셔너리명['키명']
#print(dic1["name1"])  => key값 에러
print(dic1["name"]) # Lee출력

#p.100
print(dic1.get('name1')) #키값 없으면 None
print(dic1.get('name'))

print(dic2[0]) #python 출력
print(dic2.get(0)) 

print(dic3['ary']) # [1,2,3,4]
print(dic3.get('ary'))# [1,2,3,4]

print(dic4.get('age')) #22출력

#마지막 값만 출력됨 key값은 중복이 안됨 
a = {1 : 'c', 1 : 'a', 1: 'b', 1:'d'}
print(a) 
#딕셔너리 값 추가
dic1['address'] = 'yongsan'
print(dic1)

#dic1에 키 score에 90,30,40 리스트로 추가
dic1['score'] = (90,30,40)
print(dic1)

print(len(dic1),len(dic2),len(dic3),len(dic4))

#p.98 딕셔너리 관련 함수
print(dic1.keys())
#키값을 리스트형태로 나타내주는데 key는 고유값이므로 리스트에서 사용하는 append, insert, pop, remove, sort 사용 불가
#dict_keys(['name', 'phone', 'birth', 'address', 'score'])
print(dic2.keys())


print(list(dic1.keys())) #키값만 뽑아줄건데 리스트형태로 변경할 때 list()
#['name', 'phone', 'birth', 'address', 'score']
print(list(dic3.keys()))

print(dic1.values())
#dict_values(['Lee', '010-1234-5678', '000211', 'yongsan', (90, 30, 40)])
#value값을 리스트형태로 변경할 때 list()
print(list(dic1.values()))

print(dic3.items()) #키, 값 쌍 다 출력
print(list(dic3.items()))

#pop
print(dic1.pop('name')) #키값 넣어서 삭제 -> value도 같이 삭제됨

print(dic4.pop('addr'))
print(dic4)

#101p in()

print('name' in dic1) #False

#1. odd=[1,3,5,7,9]에서 1,3 각각 출력후 10을 1이 있는 자리에 대입한다.
odd = [1,3,5,7,9]
print(odd[0])
print(odd[1])
odd[0] = 10
print(odd)

#문제2
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#리스트를 합쳐본다
print(a + b)
#a리스트에 마지막 요소에 6을 추가한다
a.append(6)
print(a)
#인덱스 3에다 정수 7을 삽입
a.insert(3,7)
print(a)
#맨 마지막 값을 삭제해본다
a.pop()
print(a)
#인덱스 3을 삭제한다
del a[3]
print(a)
#숫자 4를 삭제한다
a.remove(4)
print(a)
#숫자 5의 위치를 알아낸다
a.index(5)

#리스트, 튜플, 딕셔너리, 집합

#102p
s1 = set()
s2 = set([1,2,3,4]) #리스트 자료형을 집합 자료형으로 변환
s3 = set([1,4,6,7])
s4 = set([1,2,'apple','mango','python'])
s5 = {'phone' , 'computer', 'notebook', 'water','phone'}
s6 = {12, 'mouse',(1,2,3), 3.14}

#s2를 튜플로 변환 tuple()
t = tuple(s2)
print(t, type(t))

#튜플로 변환했기 때문에 인덱스 사용가능
print(t[0], t[1:3])


#s3, s4를 리스트로 변환
li_test1 = list(s3)
li_test2 = list(s4)

#리스트로 변환했기 때문에 인덱스 사용가능
print(li_test1 , li_test2)
print(li_test1[0], li_test2[1:3])


set1 = set([1,2,3,4,5,6]) 
set2 = set([4,5,6,7,8,9])


#p.103~104
print(set1 & set2) # 4,5,6 출력
print(set1.intersection(set2)) # 중복 제거된 4,5,6,7,8,9출력

print(set1 | set2)#요소 중복제거 되면서 합쳐짐
print(set1.union(set2))

print(set1 - set2) #{1,2,3} set1에는 있지만 set2에 있는 요소들
print(set1.difference(set2))

#중복 요소 확인(두 집합에 공통 요소 없으면 true, 있으면 false) .isdisjoint()
print(set1.isdisjoint(set2)) 

#부분집합 set1의 모든 요소가 set2에 있는 지 확인 .issubset()
print(set1.issubset(set2))

#set1이 set2의 모든 요소를 포함하냐? issuperset()
print(set1.issuperset(set2))


#p.105
a=set([1,2,3,4])

a.add(5) #5를 추가한다
print(a)

a.remove(2)
print(a)
#a.remove(6) #없는 값 삭제 -> keyError
#print(a)

a.discard(3)
print(a)

a.clear() #다 제거(요소만 사라진다. 구조는 남아있음)
print(a)

a.update([1,2]) #값 여러개추가
print(a)

#111.p ~
a = [1,2,3]
#a는 리스트 [1,2,3]이 저장되어 있는 메모리 주소값을 가지고 있음(reference)
print(id(a))


n = 100 
print(type(n)) # 타입은 int
print(id(n)) # 주소값은 지금 컴퓨터 기준 2108805025104

a = b = c = d = 100 # a,b,c,d 모두 100

n = 50 #n을 50으로 덮어 씀

#114.p copy모듈 복사하기
#form 모듈명 import 함수명
from copy import copy
a2 = [1, 2, 3] #복사를 했지만 요소만 복사 / 주소값은 복사하지 않음
b2 = copy(a2) #b2는 a2를 복사해서 새로운 객체가 생성됨

print(a2)
print(b2)

print(b2 is a2) #false
print(id(a2)) #주소값 : 2108810389568
print(id(b2)) #주소값 : 2108810391040




#p.247
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
#모두 같은 값을 가져서 주소값이 모두 같음

x = 3
y = 5
x,y = (y,x) #언팩킹 묶인걸 풀어주는 작업
print(x)
print(y)



#문제 5, 6
#"에릭은 20살의 0.5시력이며 학점은 A이다" 라는 문자열을 format함수, f-string 로 각각 작성해라.
age = 20
name = "에릭"
score = 'A'
sight = 0.5
#format 함수
print('{}은 {}살의  {} 시력이며 학점은 {}이다'.format(name,age,sight,score))
#f-string
print(f'{name}은 {age}살의  {sight}시력이며 학점은 {score}이다')

#names 리스트에 "찰스, 스누피, 루피"를 넣는다. "찰스는 파이썬 배워요" 를 출력해라.
names = ['찰스','스누피','루피']
print(f"{names[0]}는 파이썬 배워요")

kor = 80
eng = 75
math = 55
print((kor + eng + math) / 3)

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

listA = [1, 3, 5, 4, 2]
listA.sort()
print(listA)
listA.reverse()
print(listA)


#초기 조건 증감
#while 조건 :
#반복할 실행코드

num = 5 
while num > 0 : 
    print(num)
    num  = num -1 #1씩 감소

a = ['a', 'b','c','d']
while a: #리스트안에 a라는 값이 있으므로 True로 인식
    print(a.pop())

n = 10 #초기값
while n > 0 :
    n -=1 #반복할 문장
    if n == 2:
        break #반복문 탈출
    print(n) #10 9 8 7 6 5 4 3(2부턴 break이므로 출력X)

n1 = 10
while n1 > 0 :
    print(n1) #여기선 2가 출력되는데 이유는 0 > 2를 비교하기 때문에 출력
    n1 -=1
    if n1 == 2: 
        continue #제외 (n==2이면 반복문 다시 실행)
    print(n1) # 여기선 2가 출력되지 않음 why? continue때문에


pocket = ['paper','cellphone'] #리스트
#리스트 중복 가능 순서 유지
card = True
if 'money' in pocket:
    print('택시를 타고 가라') #money가 pocket 리스트에 없는 상태
else:
    if card: # card = True 참조
        print("택시를 타고 가라") #출력
    else:
        print("걸어가라")

#복잡하게 보이는 코드를 바꾸기위해 다른 조건을 추가하는 elif() 자바스크립트 : else if()
card = True
if 'money' in pocket: #포켓리스트에 머니가 있다면
    print('택시를 타고 가라') 
elif card: # card = True # 주머니에 머니가 없고 카드가 있다면 card = False면
    print("택시를 타고 가라") #출력
else: # 둘다 없는 쌉그지면
    print("걸어가라") 
#위에 서로 코드 비교해보기


i = 1 #초기값
while i <= 10: #i는 1부터 10보다 작거나 같을 때까지
    print(i) 
    if i == 5: # i가 5이면 
        break # 종료
    i += 1 #들여쓰기를 보면 while문 안에 +1이 있음 
#들여쓰기 진짜 중요 자바스크립트로 따지면 -> { }


a1 = ['water','python','java', 'phone']
s1 = 'py'
i = 0

#리스트 끝까지 py랑 같은지 확인하는 코드 -> 같으면 반복문 종료시킴
#while 뒤의 else는 루프가 break 없이 끝났을 때만 실행된다!
#while ~ else 구문 (while루프가 정상적으로 끝났을 때만 else블록 실행시킴) break로 루프 중간에 종료되면 else실행 안됨
while i < len(a1): #i(= 0)가 a1의 길이인 4보다 작을 때까지
    if a1[i] == s1:
        break
    i+=1
else : #else를 while과 짝을 이룸
    print('hi')

#무한루프
#while True : 빠져나갈 조건을 추가해줘야 사용가능
li = ['a','b','c']
while True : #무한 루프 안에서
    if not li: #li리스트에 값이 없으면
        break #탈출
    print(li.pop()) #li리스트에 값이 있으면 끝에서부터 출력

#1. 1~10 까지 수 중 짝수만 출력 (반복문 활용)
a = 1
while a < 10:
    a += 1
    if a%2 == 0:
        print(a)
#dic={'name':'tom','age':'11'} subject를 python으로 추가한다 name 을 삭제한다
dic = {'name' : 'tom', 'age' : '11'}
dic['subject'] = 'python'
print(dic)

#3. [1,2,3]을 집합자료형으로 바꾼다
b = set([1,2,3])
print(type(b))

#4. 문자열 python을 list자료형으로 바꾼다
py = list("python")
print(type(py))

#5. s4=set([1,2,3,4,5]) s5=set([6,7,3,4,10]) 교집합, 합집합을 구해라
s4 = set([1,2,3,4,5])
s5 = set([6,7,3,4,10])
print(s4 & s5)
print(s4.union(s5))
print(s4 | s5)

n = 1
while n <= 10:
    if(n%2 == 0):
        print(n)
    pass #else생략 if문과 같은 라인 반대표시
    n+=1