num = input("숫자 : ")

print("숫자" + num + "를 입력하셨습니다")
# num이 int 타입이었다면 형변환 필요

scores = {"math" : 0, "eng" : 50, "coding" : 100}

# ljust, rjust : 공간 확보 하기
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# zfill()
org = "hello" # +나 -가 있으면 그 뒤로 0이 채워짐
print(org.zfill(10)) # 음수가 들어가면 그냥 문자열 반환

# format()
print("{0: >+10}".format(500))
# 숫자 500에 대해 10칸 확보, 양수면 + 기호, 왼쪽 정렬, 공백은 빈칸으로 두기