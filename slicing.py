jumin = input('당신의 주민등록번호를 입력해주세요 : ')

name = input('당신의 이름을 입력해주세요 : ')
gender = int(jumin[7])
years = int(jumin[0:2])
age = int(121-years)
date = jumin[2:4]
day = jumin[4:6]

# 성별 구분
if gender == 1:
    print(f'{name}의 성별 : 남')
elif gender == 2:
    print(f'{name}의 성별 : 여')


print(f'{name}씨의 나이 : {years}년생, {age}입니다.')
print(f'태어날 월 : {date}월, 태어난 일 : {day}일')

# 한국 군대
if gender == 1 and 20 <= age <= 22 :
    print(f'{name}씨는 지금 군인입니다.')
elif gender == 1 and 1 <= age <= 19 :
    print(f'{name}씨는 현역 대상자가 아닙니다.')
elif gender == 1 and 23<= age < 100 :
    print(f'{name}씨는 예비역 입니다.')





