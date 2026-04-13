#1. 두개의 정수를 입력 받아서 두 수의 차를 출력하는 프로그램을 구현해보자. 단 큰 수를 먼저 입력해야한다.
a=int(input("첫번째 정수입력 : "))
b=int(input("두번째 정수입력 : "))
print(a-b)

#2. 숫자 하나를 입력받고 "양수""음수"를 출력해보세요.
userInput=int(input("숫자 입력 : "))
if userInput > 0:
    print("양수")
elif userInput == 0:
    print("양수도 음수도 아님")
else:
    print("음수")

#3. 숫자 하나를 입력 받고 "짝수""홀수"를 출력해보세요.
userInput=int(input("숫자 입력 : "))
if userInput % 2 == 0:
    print("짝수")
else:
    print("홀수")

#4. 0-99점까지 있는 과목 3개의 점수를 입력 받고 총합과 평균을 구한다음 평균이 60이 넘으면 합격 미만이면 불합격을 출력하세요. 단. 한 과목이라도 60미만이라면 불합격 (70,70,9)=> 불합격
a=int(input("첫번째 점수 입력 : "))
b=int(input("두번째 점수 입력 : "))
c=int(input("세번째 점수 입력 : "))
total=a+b+c
average=total/3
if average >= 60:
    print(a,b,c ,"=> 합격")
elif a<60 or b<60 or c< 60:
    print(a,b,c , "불합격")
else:
    print(a,b,c ,"=> 불합격")

#5. 정수 2개를 입력 받고 나눈 "몫"과 "나머지"를 출력 만약에 둘 중 하나라도 0이면 "0으로 나눌 수 없다"출력
a=int(input("첫번째 정수 입력 : "))
b=int(input("두번째 정수 입력 : "))
if a ==0 or b == 0:
    print("0으로 나눌 수 없다.")
else:
    print("몫 : ",a//b,"나머지 : ",a%b)

#6. 학생의 전체 평균점수에 대한 학점을 출력하는 프로그램을 작성해보자. 학생의 성적이 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C,60점 이상이면 D, 그리고 그 미만이면 F다.
userInput=int(input("학생 평균 점수 : "))
if userInput >= 90:
    print("A")
elif userInput >= 80:
    print("B")
elif userInput >= 70:
    print("C")
elif userInput >= 50:
    print("D")
else:
    print("F")

#7. 나이에 따른 결과를 출력하는 프로그램을 완성하시오. (0-7:미취학아동, 8-13: 초등학생, 14-16:중학생, 17-19ㅣ 고등학생, 20~: 성인)
userInput=int(input("나이 입력 : "))
if 0<=userInput<=7:
    print("미취학아동")
elif 8<=userInput<=13:
    print("초등학생")
elif 14<=userInput<=16:
    print("중학생")
elif 17<=userInput<=19:
    print("고등학생")
elif userInput >= 20:
    print("성인")
else:
    print("존재하지 않음")


#8. 윤년 판단하기
    #윤년은 연도가 4의 배수이면서, 100의 배수가 아닐때 또는 400의 배수일때이다. 예를 들어, 2012년 4의 배수이면서 100의 배수가 아니라서 윤년이다.
    #1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 2000년은 400의 배수이기 때문에 윤년이다.
userInput=int(input("연도 입력 : "))
if (userInput % 4== 0 and userInput % 100!= 0) or userInput % 400 == 0:
    print(userInput ,"은/는 윤년이다")
else:
    print(userInput ,"은/는 윤년이 아니다")

#9,점수 하나를 입력 받고 60점 이상이면 "합격", 60점 미만이면 "불합격"을 출력해보시오.
userInput=int(input("점수 입력 : "))
if userInput >= 60:
    print("합격")
else:
    print("불합격")


#print 사용 방법
# print("두수의 값은 : ", a+b. "입니다.")
# print("{0}+{1}={2}".format(a,b,a+b))
# print("%d+%d=%d"%(a,b,a+b))
# print(f"{a}+{b}={a+b}")

a=[1,2,3,4] #list
print(5 in a) #a라는 list에 5라는 값이 있니?

a=10
while a>0: #난 이 조건을 실행하겠다 이 조건이 거짓을 만족할때까지
    print(f"a의 값은 : {a}입니다.")
    a=a-1

a=10
while True: #해당 조건이 반복적으로 실행된다.
    print(f"a의 값은 : {a}입니다.")
    a=a-1




#10.1~10까지 출력하기
a=1
while a<=10:
    print(a)
    a=a+1

#11. 10부터 1까지 출력하라.
a=10
while a>=1:
    print(a)
    a=a-1

#12. 1~100사이의 모든 3의 배수만 출력하라.
a=1
while a<=100:
    if a%3==0:
        print(a)
    a=a+1

#13. 1~100사이의 모든 3의 배수 합을 출력하라.
a=1
total=0
while a<=100:
    if a%3==0:
        total=total+a
    a=a+1
print(total)



#14. 사용자로부터 정수 한개를 입력 받아서 1부터 입력받은값까지의 합계를 출력하는 프로그램을 작성하시오.
userInput=int(input("정수 입력 : "))
a=1
total=0
while userInput>=a :
    total=total+a
    a = a + 1
print(f"합계 : {total} 이다.")