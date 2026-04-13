#지난주 과제
print("정수:",1,"문자 :","ABC","실수:",3.14)
print("정수 : %d 문자 : %s 실수 : %0.2f" % (1, "ABC", 3.14)) #소숫점 둘째자리까지 출력을 해준다.
print("정수 : {0} 문자 : {1} 실수 : {2}". format(1,"ABC",3.14))
print(f"정수 : {1} 문자 : {"ABC"} 실수 : {3.14}")
a=10
b="ABC"
c=3.14
print(f"정수 : {1} 문자 : {"ABC"} 실수 : {3.14}") #해당 형태가 현재 많이 사용하는 형태

a="abcdcefc"
print(a.count("c")) #a.count는 a라는 문자 안에서 문자열 c의 개수
print(len(a)) #len은 이 변수의 길이를 물어보는 것

a="abcdecfc"
b=",".join(a)
print(b)

a=[4,2,1,"ABC",3]
print(type(a)) #a의 속성을 알려주고 있는것)
b="3.14"
print(type(b))

a=[4,2,1,"ABC",3] #앞에서부터 0을 가르킴
print(type(a))
print(a[3][1]) #3번째거 중에서 1번째
print(a[2])

a=[1,2,3,4,5]
b=a[:2] #처음부터 a[1] (=2바로 전까지)까지
c=a[2:]
print(b)
print(c)

a=[1,2,3,4,5]
print(a[:2])
print(a[2:])
b=[7,8,9]
c=a+b*3
print(c)
a[2]=3.14
print(a)
del a[3]
print(a)

a=[1,2,3,4,5]
print(a)
a[1]=10
a.sort()
print(a)
a.sort(reverse=True)
print(a)



a={"A+" : 4.5, "A" : 4.0, "B+" : 3.5}
a["B-"] = 3.5
print(a)
print(a["A"])
a['test']='abcd'
print(a)
del a["B+"]
print(a)
print(a.keys())
print(a.values())
print(list(a.keys()))
print(list(a.items()))
print(4.5 in a)
print("A" in a)



userInput = int(input("점수입력 : "))
print(userInput+5)

#1,정수 하나 입력받아서 60점 이상이면 합격을 출력하세요.
userInput=int(input("점수입력 : "))
if userInput >= 60:
    print("합격")
else :
    print("불합격")
print("프로그램 종료")

#2.정수하나를 입력받아서 90이상이면 A, 80이상이면 B, 70이상이면 C, 60이상이면 D, 60미만이면 F를 출력하는 프로그램 작성
userInput=int(input("점수입력 : "))
if userInput >= 90:
    print("A")
elif userInput >= 80:
    print("B")
elif userInput >= 70:
    print("C")
elif userInput >= 60:
    print("D")
else :
    print("F")


#3,정수 두개 연산자 한개를 입력 받아서 출력하는 프로그램을 작성
a=int(input("첫번째 수 입력 : "))
b=int(input("두번째 수 입력 : "))
c=input("연산자 입력 :")
if c == "+":
    print("결과는",a+b,"입니다.")
elif c == "-":
    print("결과는",a-b,"입니다.")
elif c == "*":
    print("결과는",a*b,"입니다.")
elif c== "/":
    print("결과는",a/b,"입니다.")
else :
    print("엉뚱한 기호를 넣었습니다.")

#4,정수 두개 연산자 한개를 입력 받아서 출력하는 프로그램을 작성 (교수님답안) -> 이거 지워야 내꺼 구동
firstinput=int(input("첫번째 수 입력 :"))
secondinput=int(input("두번째 수 입력 : "))
op=input("연산자 입력 : ")
if op == "+":
    result =firstinput + secondinput
elif op == "-":
    result =firstinput - secondinput
elif op == "*":
    result =firstinput * secondinput
elif op == "/":
    result =firstinput / secondinput
else:
    print("엉뚱한 기호를 넣었습니다.")
print(f"{firstinput},{op}, {secondinput}= {result}")


#5,정수 한 개를 입력받아서 짝수인지 홀수인지 판별하는 프로그램을 작성하시오.
userInput = int(input("정수를 입력하세요 : "))
if userInput % 2 == 0:
    print(userInput,"은 짝수입니다.")
else:
    print(userInput,"은 홀수입니다.")


