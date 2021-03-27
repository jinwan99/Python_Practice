subway = ["유재석","조세호","박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 지하철에 탔음
subway.append("하하")
print(subway)
# append를 하면 항상 List맨 뒤에 붙는다

# 정형돈을 유재석 / 조세호 사이에 탸워봄
subway.insert(1 , "정형돈") # 1번 위이에 정형돈이 들어간다.
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway) # pop을 하고 남은 사람 보기

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 유재석이 몇 번 나오는지 검색

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기도 가능
num_list.reverse()
print(num_list)

# 리스트의 내용 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장 (List1 + List2 개념)
num_list.extend(mix_list)
print(num_list)

