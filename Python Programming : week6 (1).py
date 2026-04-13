# #1. 사용자로부터 가위바위보를 입력 받ㅇ, 컴퓨터와 가위바위보하는 게임을 만들어보세요. 동시에, 총 세번 먼저 이기면 최종 승리하는 삼세판 규칙을 구현해보세요
import random
z=["가위","주먹","보"]

win=0

while True:
    com=random.choice(z)
    print("컴퓨터의 값 :",com)
    user=input("가위, 주먹, 보 중 하나를 입력하세요 : ")
    if user==com:
        print("비김")
    elif (user=="가위" and com == "보") or (user == "주먹" and com == "가위") or (user == "보" and com == "주먹"):
        print("승리")
        win=win+1
        if win == 3:
            break
    else :
        print("패배")


#2. 사용자로부터 문자열을 입력 받아, 혼자서 하는 끝말잇기 게임을 만들어보세요. 단 두음법칙은 적용되지 않으며, 0을 입력하거나 이미 앞에서 사용한 단어이거나 답이 틀렸을 경우에는 게임이 종료되게 해주세요.
myList=[]

while True:
    userInput=input("단어를 입력하세요(0은 종료) : ")

    if userInput == "0":
        print(myList)
        break
    if userInput in myList:
        print("같은 단어가 있습니다. 패배", myList)
        break

    if len(myList)>0:
        if myList[-1][-1] == userInput[0] :  #[사과,과자]일때 과자의 끝값인 자가 나온다
            myList.append(userInput)
        else:
            print(f"마지막 철자가 '{myList[-1][-1]}'입니다. 패배")
            break
    else:
        myList.append(userInput)
