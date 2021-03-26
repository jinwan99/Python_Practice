# Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성
#ex) http://naver.com
# rule1 ) http:// 부분은 제외 -> naver.com
# rule2 ) 처음 만나는 점(.) 이후 부분은 제외 -> naver
# rule3 ) 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성
#                  (nav)             (5)             (1)        (!)
# ex) 생성된 비밀번호 : nav51!

message = input('비밀번호를 만들 사이트URL 입력 : ')

# find / index
fi = message.index('/')
fi = message.index('/', fi+1) # 처음 지정할 때 message[fi+1:]로 지정

dot_fi = message.index('.') # 마지막 지정할 때 message[:dot_fi]로 지정

# 처음과 마지막 결과 합치지
fi_dot_fi = message[fi+1:dot_fi]

# 남은 글자 중 처음 세자리
three_character = fi_dot_fi[:3]
# 글자 갯수
length_character = len(fi_dot_fi)
# 글자 내 'e' 갯수
counter_e = fi_dot_fi.count('e')

# 결과 전부 합치기
result = three_character + str(length_character) + str(counter_e) + '!'
print(result)