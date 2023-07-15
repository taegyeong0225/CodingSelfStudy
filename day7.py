# 튜플 : 리스트의 읽기 전용 버전 느낌 (추가, 삭제, 변경 불가, 대신 속도가 빠름), () 형식
# a = 1
# b = 2
# c = 3
a, b, c = 1, 2, 3 # 튜플 형태로 한 줄에 여러 변수의 값을 정의한 것, 튜플 할당
(a, b) = (b, a) # 쉽게 값 변경 가능

# 세트 : 집합!!! 중복 허용 X, 데이터 순서 보장 X, 중괄호로 정의
set1 = {1, 2, 3, 3} # 1, 2, 3
set2 =  set([1, 2, 3, 4])
print(set1 & set2) # 교집합1
print(set1.intersection(set2)) # 교집합2
print(set1 | set2) # 합집합1
print(set1.union(set2)) # 합집합2
print(set2 - set1) # 차집합1
print(set2.difference(set1)) # 차집합2
set1.add(5) # 추가, 삭제는 remove()

# 자료구조의 변환
# 자료구조(자료구조변수) 형식
list = list(set1)
