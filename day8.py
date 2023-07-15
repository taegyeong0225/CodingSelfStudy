# 학점 산출 프로그램 (조건문)
grade = 95

if grade >= 95:
    print("A+")
elif grade >= 90:
    print("A")
elif grade >= 85:
    print("B+")
elif grade >= 80:
    print("B")
elif grade >= 75:
    print("C+")
elif grade >= 70:
    print("B")
else:
    print("F")

print("============================")

# 날씨 출력
whether = input("오늘의 날씨 : ")
if whether == "비":
    print("우산을 챙기세요")
elif whether == "황사":
    print("KF94 마스크를 챙기세요")