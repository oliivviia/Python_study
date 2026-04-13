#정수 한 개를 입력받아서 짝수인지 홀수인지 판별하는 프로그램을 작성하시오.
userInput = int(input("정수를 입력하세요 : "))
if userInput % 2 == 0:
    print(userInput,"은 짝수입니다.")
else:
    print(userInput,"은 홀수입니다.")
