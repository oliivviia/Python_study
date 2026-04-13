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