# 수강 신청의 중복 과목 없애기
enlol_list = ['자료구조', '알고리즘', '운영체제', '운영체제']

enlol_set = set(enlol_list)
enlol_list = list(enlol_set)

print("신청한 과목은 다음과 같습니다.")
print(enlol_list)