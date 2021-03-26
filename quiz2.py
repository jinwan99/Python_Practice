# Quiz) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성
#ex) http://naver.com
# rule1 ) http:// 부분은 제외 -> naver.com
# rule2 ) 처음 만나는 점(.) 이후 부분은 제외 -> naver
# rule3 ) 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성
#                  (nav)             (5)             (1)        (!)
# ex) 생성된 비밀번호 : nav51!

site_name = 'http://naver.com'

# rule1 )
rule1 = site_name[7:]

# rule2 )
rule2 = rule1[:-4]

# rule3 )
rule3 = rule2[:3]
num = str(len(rule2))
e_count = str(rule3.count('e'))
print(rule3+num+e_count+'!')