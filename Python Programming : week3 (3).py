userInput = int(input("점수입력 : "))
print(userInput+5)

#정수 하나 입력받아서 60점 이상이면 합격을 출력하세요.
userInput=int(input("점수입력 : "))
if userInput >= 60:
    print("합격")
else :
    print("불합격")
print("프로그램 종료")

#정수하나를 입력받아서 90이상이면 A, 80이상이면 B, 70이상이면 C, 60이상이면 D, 60미만이면 F를 출력하는 프로그램 작성
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




