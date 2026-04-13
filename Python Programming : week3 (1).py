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

