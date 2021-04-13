# Dictionary -> key : value
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

# cabinet.get(n) = cabinet[n]
print(cabinet.get(3))

# print(cabinet[5])
# print('hi') # 이거 출력 안됌

print(cabinet.get(5)) # 이건 출력된다.
print(cabinet.get(5, "사용 가능")) # 이렇게 하면 key : value가 된다.
print('hi')

print(3 in cabinet) # 3이라는 것이 cabinet에 있으면 True
print(5 in cabinet) # 5라는 것이 cabinet에 없으면 False

# key는 정수가 아닌 String도 가능하다.
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님이 온경우
print(cabinet)
cabinet["A-3"] = "김종국" # 유재석이 빠지고 김종국이 가지게된다.
cabinet["C-20"] = "조세호" # 없는 key에 대해서는 추가가 된다.
print(cabinet)

# 간 손님
del cabinet["A-3"] # 김종국이 삭제됨
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # 모든 값을 지울 수 있다.
print(cabinet)