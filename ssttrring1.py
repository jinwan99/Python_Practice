python = "Python is Amazing"
print(python.lower())
print(python.upper())

# python[0]이 대문자인 경우 True / 아닌경우 False
print(python[0].isupper())

# 문자열의 길이
print(len(python))

# Python문자를 찾아서 다른 문자열로 바꾸기
print(python.replace("Python","Java"))

# 어떤 문자가 어느 번째에 존재하는지 -> 결과 5 (0번부터 카운터)
index = python.index("n")
print(index)
# 위에 n다음에 있는 n은 몇 번째에 있는지 찾기 -> 결과 15
index = python.index("n", index+1)
print(index)

# index이외의 다른 함수는?
print(python.find("Java")) # 문자열 함수 find라는 것도 있다. -> 결과 -1이 출력된다. (에러가 나도 실행됨)
print("hello") # hello는 출력됨
print(python.index("Java")) # 결과는 에러가 나온다. -> 다음 결과 실행 안됌
print("hi") # hi는 출력이 안됨

print(python.count("n")) # n이 총 몇번 등장하는지