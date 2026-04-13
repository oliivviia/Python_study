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