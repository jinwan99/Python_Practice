# continue and break문

absent = [2,5] # 결석한 학생번호
no_book = [7] # 책을 안가져온 학생번호
for student in range(1,11): # 1~10까지 출석번호 존재
    if student in absent: # student안에 absent가 있을 경우
        continue
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
        break
    print(f"{student}, 책을 읽어봐")