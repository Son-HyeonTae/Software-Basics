# 201811302 손현태 기말프로젝트
# 월드컵 시뮬레이션 프로그램

import turtle   # 터틀그래픽
t=turtle.Turtle()
t.shape("arrow")
t.speed(300)   # 터틀 속도 빠르게

import time, random, datetime   # "time, random, datetime 모듈" import
now = datetime.datetime.now()

from tkinter import *   # Tk인터페이스

win = ""   # Global variable (전역변수)

#---------------------  함수 모듈  ---------------------

def pause() :
    time.sleep(3)   # 프로그램 3초 정지 → 몰입감 강화

def playGame(T1, T2) :   # 게임실행함수(Team1, Team2)
    s1 = random.randrange(8)   # 0~7 숫자 랜덤 생성
    s2 = random.randrange(8)
    s3 = random.randrange(2)   # 0, 1 동전 던지기
    if s1 > s2 :   # "T1승리" or "T2승리" or "동점" 결과 분류를 위한 "if-elif-else"문
        t.write("경기결과 : " + str(s1) + ":" + str(s2) + ", " + str(T1) + " 승리")   # "t.write()함수"로 텍스트 제공
        global win   # Global variable (전역변수)로 함수 밖으로 정보 이동
        win += "A"  # win변수 끝에 문자열 추가
    elif s2 > s1 :
        t.write("경기결과 : " + str(s1) + ":" + str(s2) + ", " + str(T2) + " 승리")
        win += "B"
    else :
        t.write("경기결과 : " + str(s1) + ":" + str(s2) + " 무승부.")
        pause()
        if s3 == 0 :   # 동전던지기 결과 분류를 위한 "if-else"문
            window = Tk()
            l1 = Label(window, text = "동전던지기 → " + str(T1) + " 승리")
            l1.pack()   # Tk 인터페이스 출력
            win += "A"
        else :
            window = Tk()
            l2 = Label(window, text = "동전던지기 → " + str(T2) + " 승리")
            l2.pack()
            win += "B"

#--------------------- 터틀 그래픽 ---------------------

t.penup()
t.goto(-250, -100)
t.pendown()
t.left(90)
t.forward(50)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.penup()
t.goto(50, -100)
t.pendown()
t.right(180)
t.forward(50)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.penup()
t.goto(-175, -50)
t.pendown()
t.right(180)
t.forward(50)
t.right(90)
t.forward(300)
t.right(90)
t.forward(50)
t.penup()
t.goto(-25, 0)
t.pendown()
t.right(180)
t.forward(50)

for x in range(-230, 221, 150) :   # 팀 위치 반복 그리기를 위한 "for 반복"문
    t.penup()
    t.goto(x, -100)
    t.pendown()
    t.color("blueviolet")   # "t.color() 함수"로 색상지정
    t.begin_fill()
    t.circle(20)   # 원 그리기
    t.end_fill()
for x in range(-155, 146, 300) :
    t.penup()
    t.goto(x, 0)
    t.pendown()
    t.color("dodgerblue")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
t.penup()
t.goto(-5, 50)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(20)
t.end_fill()

#--------------------- 게임 준비 ---------------------

name = turtle.textinput("", "주최자 이름을 입력해주세요.")   # 주최자 입력을 위한 "turtle.textinput()"
t.penup()
t.goto(-55, -140)
t.pendown()
t.color("black")
t.write(str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일")   # 현재날짜 출력
t.penup()
t.goto(-91, -150)
t.pendown()
t.write("★★★ " + name + " 배 월드컵 ★★★")   # 대회명 출력

team_list = [ ]   # 4개 팀 list[]
count = 1
for count in range(1, 5) :
    team = turtle.textinput("", str(count)+"번째 팀 이름을 입력해주세요.(2글자 권장)")   # 팀명 입력을 위한 "turtle.textinput()"
    team_list.append(team)   # 팀명 할당

i = 0   # "Index 값"
for x in range(-260, 191, 150) :   # 팀 이름 반복 배치를 위한 "for 문"
    t.penup()
    t.goto(x, -110)
    t.pendown()
    t.write(team_list[i])   # "Index 값"이 반영된 list[] 출력
    i = i + 1

#---------------------   게임 시작   ---------------------
#--------------------- 준결승 1차전 ---------------------
    
t.right(180)

t.penup()
t.goto(-240, -65)
t.pendown()
t.write("준결승 1차전 = " + team_list[0] + " vs " + team_list[1])
pause()
t.penup()
t.goto(-240, -80)
t.pendown()
playGame(team_list[0], team_list[1])   # playGame() 사용자 지정 함수 사용
if win == "A" :
    final1 = team_list[0]   # 첫번째 승리 팀 할당
    t.penup()
    t.goto(-185, -10)
    t.pendown()
    t.write(team_list[0])
else :   # win == "B"
    final1 = team_list[1]   # 첫번째 승리 팀 할당
    t.penup()
    t.goto(-185, -10)
    t.pendown()
    t.write(team_list[1])

#--------------------- 준결승 2차전 ---------------------

t.penup()
t.goto(60, -65)
t.write("준결승 2차전 : " + team_list[2] + " vs " + team_list[3])
pause()
t.penup()
t.goto(60, -80)
t.pendown()
playGame(team_list[2], team_list[3])
if win == "AA" or win == "BA" :   # 첫번째 경기결과 이후, 두번째 경기결과에 대한 논리연산
    final2 = team_list[2]   # 두번째 승리 팀 할당
    t.penup()
    t.goto(115, -10)
    t.pendown()
    t.write(team_list[2])
else :   # win == "BA" or win == "BB"
    final2 = team_list[3]   # 두번째 승리 팀 할당
    t.penup()
    t.goto(115, -10)
    t.pendown()
    t.write(team_list[3])

#---------------------     결승전     ---------------------

t.penup()
t.goto(-75, -15)
t.write("결승전 : " + final1 + " vs " + final2)
pause()
t.penup()
t.goto(-75, -30)
t.pendown()
playGame(final1, final2)
if win[-1:] == "A" :   # "AAA" or "ABA" or "BAA" or "BBA" 를 간략화 하기 위한 "문자열 Slice"
    winner = final1   # 우승 팀 할당
    t.penup()
    t.goto(-35, 40)
    t.pendown()
    t.write(final1)
elif win[-1:] == "B" :   # "AAB" or "ABB: or "BAB" or "BBB" 를 간략화 하기 위한 "문자열 Slice"
    winner = final2   # 우승 팀 할당
    t.penup()
    t.goto(-35, 40)
    t.pendown()
    t.write(final2)
t.penup()
t.goto(-25, 75)
t.pendown()
t.write("우승팀 : " + str(winner) + " ★축하합니다!!★")   # 우승 팀 출력
