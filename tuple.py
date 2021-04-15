# 튜플은 리스트와는 다르게 변경할 수가 없다. 하지만 속도가 빠르다.
menu = ("돈가스","치즈가스")
print(menu[0])
print(menu[1])
# menu.add("생선가스") <- 이거 에러가 난다. 튜플은 추가/변경이 안된다.

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)