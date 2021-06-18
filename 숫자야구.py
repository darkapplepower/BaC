import random
def checkNum(num, leng):
    if not num.isdigit() or not len(num)==leng:
        return False
    else:
        j=[]
        for i in num:
            if i in j:
                return False
            j.append(i)
        return True
def BnS(num1, num2, leng):
    result=[0, 0]
    for i in range(leng):
        if num2[i]==num1[i]:
            result[0]+=1
        elif num2[i] in num1:
            result[1]+=1
    return result
def clearconsole():
    for i in range(100):
        print()
leng=0
while (1>leng or leng>9):
    try:
        print("숫자야구 게임에서 사용할 숫자의 길이를 정해주세요")
        leng=int(input("1~9 사이의 수 입력: "))
    except:
        leng=0
        continue
playerdata=[0, 0]
for i in range(2):
    while True:
        print("player "+str(i+1)+"의 입력입니다")
        playerdata[i]=input(str(leng)+"자리의 각 자리수가 모두 다른 숫자를 입력해주세요")
        if checkNum(playerdata[i], leng):
            clearconsole()
            break
turn=random.randint(0, 1)
while True:
    turn=+(not turn)
    clearconsole()
    print("player "+str(turn+1)+"의 차례입니다")
    data=None
    while True:
        data=input(str(leng)+"자리의 각 자리수가 모두 다른 숫자를 입력해주세요")
        if checkNum(data, leng):
            break
    data=BnS(playerdata[+(not turn)], data, leng)
    if data[0]==leng:
        print("player "+str(turn+1)+"님이 상대방의 숫자를 맞췄습니다.")
        print("게임을 종료합니다.")
        break
    else:
        print(str(data[0])+"스트라이크")
        print(str(data[1])+"볼")
        input("계속하려면 엔터를 쳐주세요")
