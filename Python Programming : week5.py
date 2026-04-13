#input함수는 사용자로부터 입력받는 함수 (무조건 문자로 인식함)
#int함수는 무조건 숫자로 변환하는 함수
#a=int(input("정수입력:"))

#if 조건 : 조건은 참 또는 거짓만.

#>,<,>=,<=.==.!=(관계연산자)
#and, or (논리연산자) => 조건 and　조건

#while 조건 (True) => 무조건 참이기에 안쪽에 있는 것을 계속 수행
#a=[1,2,3]
#b=2 in a
#print(b)
#결과는 True로 나온다.

a=[1,2,3,"AA","BB",100]
for x in a:
    if x == "AA":
        break #무조건 for문에서 빠져나와라
       #continue 무조건　for문 위에 있는거
        #for안에 for이 들어가면 바깥 for　안쪽 for문에 break가 있으면, 안쪽에 있는것만 빠져나온다 (나를 감싸고 있는 가장 가까운것만)
        #for반복문 없이는 break나 continue는 사용 불가능하다
    print(x)


for i in range(2,10):
    print(i)

for i in range(1,3):
    for j in range(1,5):
        print(f"i={i}, j={j}",end=" ")
    print()




# #1.1~10까지 출력하기
for i in range(1,11):
    print(i)

# #2.10부터 1까지 출력하라
for i in range(10,0,-1):
    print(i)


# #3.1~100사이의 모든 3의 배수만 출력하라.
for i in range(3,101,3):
    print(i)


# #3=1. 사용자로부터 시작값과 끝값 및 배수의 값을 입력받아서 시작값부터 끝깝까지의 배수의 합을 출력하는 프로그램을 작성.
start=int(input("시작값 입력 : "))
finish=int(input("끝값 입력 : "))
times=int(input("배수의 값 입력 : "))

total=0
for i in range(start,finish+1):
    if i%times==0:
        total=total+i
print("최종합계는 %d이다"%total)


# #3-2. 단수를 입력받아서 해당 단수를 출력하기
times=int(input("구구단 단수 입력 : "))
for i in range(times,times*9+1,times):
    print(i)
for i in range(2,10):
    print(f"{times}+{i}={times*i}", end=" ")
print()


# #3-3. 구구단을 출력하는 프로그램을 작성하세요.
for i in range(1,10):
    for times in range(1,10):
        print(f"{i}*{times}={i*times}", end=" ")
    print()
print()


# #4.첫날은 1원, 이후 30일 동안은 전날보다 2배의 금액을 받는다. 30일 되는 날 총 금액은 얼마인지 구하기


# #5. 중첩 반복문을 이용해서 꽉 찬 사각형 출력하기
size=int(input("사이즈를 입력하세요 : "))
for i in range(size):
    for j in range(size):
        print("*",end="")
    print()

# #6. 정수를 입력 받고, 입력 받은 정수의 갯수만큼 열을 출력하며 이때, 열마다 행의 "갯수는 +1씩 추가되는 코드를 작성하라.
number=int(input("정수를 입력하세요 : "))
for i in range(1,number+1):
    for j in range(i):
        print("*",end="")
    print()
print()

# #7. 1부터 10까지의 수를 출력하세요! *단 숫자가 6일때는 출력하지 마세요!
for i in range(1,11):
    if i==6:
        continue
    print(i, end="")
print()

# #8. 하루에 독감으로 병원에 내방하는 환자 수가 50명에서 100명 사이일때, 누적 독감 환자수가 최초 10,000명을 넘을 때의 일수를 구해보자.
import random
total_patients=0
days=0
while total_patients <=10000:
    daily_patients=random.randint(50,100)
    total_patients=total_patients+daily_patients
    days=days+1
print(f"{days}일째에 누적 환자수{total_patients}명으로 10,000명을 넘었습니다.")

#9. 주민등록번호를 입력받으면 생년월일과 성별을 출력하는 픞로그램을 작성하시오. (주민등록번호 입력시 -을 포함합니다.)
jnumber=input("주민등록번호 입력 (-포함 입력) : ")
year=jnumber[0:2]
month=jnumber[2:4]
day=jnumber[4:6]
gender_code=jnumber[7]

if gender_code in ['1','3']:
    gender="남성"
elif gender_code in ['2','4']:
    gender="여성"

print(f"생년월일 : {year}년, {month}월, {day}일입니다.")
print(f"성별:{gender}입니다.")
print()

#10. 마스크 5부제는 생년의 끝자리를 기준으로 마사크를 구매할 수 있는 요일을 정한 제도입니다.
# 끝자리가 1,6인 사람은 월요일, 2,7인 사람은 화요일, 3,8인 사람은 수요일, 4,9인 사람은 목요일, 6,0인 사람은 금요일에 구매할 수 있습니다.
#사용자가 주민번호를 입력했을 때 사용자가 마스크를 구매할 수 있는 요일을 출력하게 코드를 구하시오.
name=input("이름을 입력사에요 : ")
jumin=input("주민들록번호를 입력하세요 : ")
last_number=int(jumin[1])

if last_number in [1,6]:
    day="월요일"
elif last_number in [2,7]:
    day="화요일"
elif last_number in [3,8]:
    days="수요일"
elif last_number in [4,9]:
    days="목요일"
elif last_number in [5,0]:
    days="금요일"

print(f"{name}님의 마스크 구매 가능요일은 {days}입니다.")
print()
