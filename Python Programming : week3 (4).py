#정수 두개 연산자 한개를 입력 받아서 출력하는 프로그램을 작성
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

#정수 두개 연산자 한개를 입력 받아서 출력하는 프로그램을 작성 (교수님답안) -> 이거 지워야 내꺼 구동
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
