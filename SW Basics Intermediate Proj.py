# 본 프로그램은 2번 문제를 선택하여 작성하였습니다.

print("★★★경기대 렌터카★★★\n")   # 프로그램 제목을 "print"

fee = 0   # 요금 초깃값 설정
s = "미가입"   # 보험가입 초깃값 설정
insurance_fee = 0   # 보험료 초깃값 설정
driving_exp = 0   # 운전경력 초깃값 설정

grade_list = ['골드 [3% 요금할인 혜택]', '다이아 [5% 요금할인 혜택]', '플레티넘 [8% 요금할인 혜택]']   #회원등급을 "list"
grade = len(input("※회원등급을 입력해주세요.※\n<골드, 다이아, 플레티넘> : "))   # list 값을 끌어오기 위한 "len"
print("회원님의 등급 :", grade_list[grade-2])   # 글자 길이 - 2 = "Index 값"

print("")
print("<<<<<가격표>>>>>\n~  3일  : 80,000원 \n~ 14일 : 150,000원 \n15일 ~ : 하루에 20,000원")
rent_days = int(input("대여일 입력 : "))   # 대여일입력을 위한 "input"

if rent_days <= 3 :   # 대여일 기준으로 상품을 선택하는 "if-elif-else"문 / 3일 이하 상품
    fee += 80000   # 요금 추가를 위한 "복합 연산자"
elif 3 < rent_days <= 14 :   # 14일 이하 상품
    fee += 150000
else :   # 15일 이상 상품
    over_days = (rent_days - 14)   # 초과 일
    over_fee = over_days * 20000   # 초과 일수 * 20000원

    print("대여일이 15일 이상일 경우, 보험가입이 필수입니다.\n")
    print("※보험상품 안내")
    print("기본 A - \ 30,000 / 종합 B - \ 70,000 / 고급 C - \ 100,000")
    print("※미입력시, 자동 \'기본 A\' 가입 \n※고급 C 가입시, 5% 추가할인 제공\n")   # 가독성을 위한 "escape 문자"
    s = input("가입하실 상품을 입력해주세요. : ")   # 보험상품 -> 변수 s

    if s[-1:] == "B" :   # 가입 상품분류를 위한 "문자열 Slice"
        insurance_fee = 70000
        fee = 150000 + over_fee + insurance_fee    # 요금 = 15만원 + 초과금 + 보험금
    elif s[-1:] == "C" :
        insurance_fee = 100000
        fee = 150000 + over_fee + insurance_fee
    else :   # 기본 A 강제선택
        insurance_fee = 30000
        fee = 150000 + over_fee + insurance_fee

print("")
print("★★★운전경력자 추가할인 이벤트 안내★★★")
print("운전경력 5년 이상일 경우 5% 추가할인 제공 \n※보험가입 할인 중복 불가능")
driving_exp = int(input("운전경력을 입력해주세요.(년) : "))   # 운전경력 입력

if driving_exp >= 5 or s[-1:] == "C" :   # [운전경력 or 보험가입] 조건에 대한 논리연산
    if grade == 2 :   # 회원등급별 가격 산정을 위한 "if-elif-else"문
        total_fee = fee - (fee * 0.08)   # 최종요금 = 요금 - 할인금
    elif grade == 3 :
        total_fee = fee - (fee * 0.1)
    else :
        total_fee = fee - (fee * 0.13)
else :
    if grade == 2 :
        total_fee = fee - (fee * 0.03)
    elif grade == 3 :
        total_fee = fee - (fee * 0.05)
    else :
        total_fee = fee - (fee * 0.08)

print("")
print("####### 고객 영수증 #######")
print("회원님의 등급 :", grade_list[grade-2])
print("대여일 :", rent_days, "일")

if insurance_fee == 30000 :
    insurance = "기본 A"
elif insurance_fee == 70000 :
    insurance = "종합 B"
elif insurance_fee == 100000 :
    insurance = "고급 C"
else :
    insurance = s   # 변수 s = "미가입"
print("보험가입 여부 :", insurance)

print("운전경력 :", driving_exp, "년")
print("합계 요금 : ", int(total_fee), "원")   # 실수 -> 정수 자료형 변환
