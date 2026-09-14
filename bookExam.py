def is_odd(number):
    if(number%2 == 0):
        return True
    else:
        return False
print(is_odd(4))
print(is_odd(9))

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)
print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

input1 = input('첫 번째 수를 입력하세여')
input2 = input('두 번째 수를 입력하세여')

total = int(input1) + int(input2)
print(f"두 수의 합은{int(total)}")


print("you" "need" "python")
print("you" + "need" + "python")
print("you","need","python") #답
print("".join(["you","need","python"]))


#프로그램 오류 수정하기
f1 = open("./resource/test.txt", "w")
f1.write("Life is too short")
f1.close()

f2 = open("./resource/test.txt", "r")
print(f2.read())
f2.close()

user_input = input("저장할 내용을 입력하세요")
f = open('./resource/test.txt',"a")
f.write(user_input)
f.write("\n")
f.close()

#파일의 문자열 바꾸기
f = open('./resource/test.txt', "r")
body = f.read()
f.close()
body = body.replace('java','python')
f = open('./resource/test.txt', "w")
f.write(body)
f.close()