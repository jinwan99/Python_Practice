# 자료구조의 변경
menu = {"커피",'우유','주스'} # 이것은 지금 set의 형태
print(menu)

menu = list(menu)
print(menu, type(menu)) # set에서 list로 변경됨

menu = tuple(menu)
print(menu, type(menu)) # tuple로 됨