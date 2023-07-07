# 문자열은 '', ""로 묶는다
sentence1 = '나는 소년입니다.'
sentence2 = "파이썬은 쉬워요."

print(sentence1, type(sentence1))
print(sentence2, type(sentence2))
print("-------------------------")

# """ """는 보이는 그대로, java에도 존재
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)
print("-------------------------")

# index 개념
jumin = "990229-1234567"
print("성별 식별번호 : " + jumin[7])

# 슬라이싱
jumin = "990229-1234567"
print("연 : " + jumin[0:2]) # 0~ 1
print("월 : " + jumin[2:4]) # 2~ 3
print("일 : " + jumin[4:6]) # 4~ 5
print("생년월일 : " + jumin[:6]) #0~ 6
print("주민등록번호 뒷자리 : " + jumin[7:]) # 7~14
print("주민등록번호 뒷자리(뒤에서부터) : " + jumin[-7:]) # 뒤에서 7번째 위치부터 끝까지, 음수는 -1까지임 주의!!!!!
print("-------------------------")

# 문자열과 함수
python = "Python is Amazing"

print(python.lower()) # 소문자로 변환
print(python.upper()) # 대문자로 변환
print(python[0].isupper()) # 인덱스 0에 있는 값이 대문자인지
print(python[1:3].islower()) # 인덱스 1~2에 있는 값이 소문자인지
print(python.replace("Python", "Java")) # Python을 Java로 바꾸기
print("-------------------------")
find = python.find("n") # 처음 발견한 n의 인덱스
print(find) # n의 인덱스 출력
index = python.index("n") # 처음 발견한 n의 인덱스
print(index) # 'Python'에서 n의 인덱스
print("-------------------------")
find = python.find("n", find + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(find) # ' is Amazing'에서 n(인덱스15)
find = python.find("Java") # Java가 없으면 -1을 반환(출력)한 후 프로그램 계속 수행
print(find)
print("-------------------------")
index = python.index("n", index + 1) # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(index) # ' is Amazing'에서 n
index = python.index("n", 2, 6) # 인덱스 2~ 5에서 찾아 처음 발견한 n의 인덱스
print(index) # 'thon'에서 n(인덱스 5)
#index()에서는 Java가 없으면 오류가 발생하며 프로그램 종료
print("-------------------------")
print(python.count("n"))
print(python.count("v"))
print(len(python))

# 문자열 포맷팅
print("ab" + "ab")
print("ab", "ab")
# 서식 지정자
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s살입니다." % 20) # %s로도 정숫값 표현 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 값이 여럿일 때
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")


#탈출문자
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace")

#커서 이동
print("Red Apple\rPine")

#백스페이스
print("Redd\bApple")

#탭
print("Red\tApple")