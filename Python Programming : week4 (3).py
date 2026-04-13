#1~10까지 출력하기
a=1
while a<=10:
    print(a)
    a=a+1

#10부터 1까지 출력하라.
a=10
while a>=1:
    print(a)
    a=a-1

#1~100사이의 모든 3의 배수만 출력하라.
a=1
while a<=100:
    if a%3==0:
        print(a)
    a=a+1

#1~100사이의 모든 3의 배수 합을 출력하라.
a=1
total=0
while a<=100:
    if a%3==0:
        total=total+a
    a=a+1
print(total)



#사용자로부터 정수 한개를 입력 받아서 1부터 입력받은값까지의 합계를 출력하는 프로그램을 작성하시오.
userInput=int(input("정수 입력 : "))
a=1
total=0
while userInput>=a :
    total=total+a
    a = a + 1
print(f"합계 : {total} 이다.")