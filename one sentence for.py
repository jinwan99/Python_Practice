# # 한 줄로 for문을 작성하는 방법
# # 출석번호가 1 2 3 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student] # i에다가 100을 더한 값을 넣을텐데 student에 있는 아이들을 하나씩 불러서 i에 넣어서 i+100을 해라 라는 의미이다.
# print(student)

# 학생 이름을 길이로 변환
# student = ["Iron man", "Thor", "I am groot"] # Iron man -> 8 / Thor -> 4 / I am groot -> 10 이렇게 바꾸고 싶다.
# student = [len(i) for i in student]
# print(student)

# 학생이름을 대문자로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [i.upper() for i in student]
print(student)