jumin = "990120-1234567"

print("성별 : "+jumin[7])
print("연 : "+jumin[0:2])
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])

print("생년월일 : "+jumin[0:6])
# print("생년월일 : " + jumin[:6]) 랑 같은 의미가 된다.
print("뒤 7자리 : "+jumin[7:])

# 뒤 1234567 중에서 7부터 [-1]로 카운트된다. 6은 [-2]
print("뒤 7자리 (뒤에서부터) : "+jumin[-7:])