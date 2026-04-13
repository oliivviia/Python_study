a=15
b=6
print(a//b)
print(a%b)
print(b*2)
print(b**2)

a="Hello world!"
b=' Sungshin Univ. '
print(a+b)
print(a*5)

a="Hello \n world!"
print(a)

a="""Hello
wor
ld!
"""
print(a)

a="Hello world!"
print(a)
b=len(a)
print(b)
print(len(a))

a=12
print(a)
print(type(a))

#두 수를 입력받아서 합을 출력하는 프로그램을 작성하세요. (문제)
a=input("정수 입력 : ") #input은 입력된걸 문자로 받아들인다
b=input("정수 입력 : ")
print(a+b)

#두 수를 입력받아서 합을 출력하는 프로그램을 작성하세요. (정답)
a=input("정수 입력 : ") #int는 문자를 정수로 바꾸는 역할을 함.
a=int(a)
b=int(input("정수 입력 : "))
print("입력한 두 수의 합은",a+b,"입니다.")

#두 수를 입력받아서 몫과 나머지를 출력하는 프로그램을 작성 (정답)
a=int(input("정수 입력 : "))
b=int(input("정수 입력 : "))
print("몫 : ",a//b, "나머지 : ",a%b, "입니다.")

a="Life is too short, You need Python" #방 번호를 인덱스라 한다.
print(a[0])
print(a[12])
print(a[-1])

a="Life is too short, You need Python"
print(a[0:6])
print(a[:6])
print(a[8:])

a="Life is too short, You need Python"
b=a[0:6]
print(a)
print(b)

print("I eat %d apples."%3)

print("I eat %s apples." %"five")

b=3
print("안녕 %d입니 %10s다." %(b,"five"))

b=3
print("안녕 %d입니 %-15s다." %(b,"five"))

b=3
print("안녕 %d 입니 %-15s다. %10.2f" % (b,"five",3.14))

print("안녕 {0}님. {1}님. {2}님 세 분 다 반가워요". format("길동","길순","철수"))

a=10
b=20
print(f"a의 값은 {a}, b의 밗은 {b}")
