# 파이썬에는 배열(고정 길이)이라는 개념이 없음

# 리스트 : 가변 길이, [] 형식, 객체임, 여러 형식 가능
station = [] # 빈 리스트 생성
station.append("사당") # 리스트 추가
station.append("인천공항")
station.insert(1, "강남") # 삽입
station.pop() # 마지막 원소 제거, 인덱스를 넣으면 인덱스 값이 제거 (없으면 에러 발생)
station.clear() # 리스트 원소 모두 제거
# station.remove("값") # 값 제거, 없으면 에러 발생
# station.count("값") : 중복 검사, station.sort() : 정렬, 값 반환 안함, sorted() 함수는 반환함
# station.reverse() : 값을 반환 안함, 원본 배열을 뒤집음
# extends() 리스트 확장

# 딕셔너리 :  key value, { : , :  } 형식
fruit = {} # 빈 딕셔너리 생성
fruit = {"apple" : "사과", "orange" : "오렌지"}
print(fruit["apple"]) # 인덱스 대신 키를 이용한다
print(fruit.get("orange")) # 인덱스 대신 키를 이용한다, 오류가 나도 프로그램이 안 죽고 None 출력
print(fruit.get("watermelon", "없습니다"))
print("apple" in fruit) # 있는지 확인
del fruit["apple"] # 값 삭제, del 키워드
print(fruit.keys())
print(fruit.values())
print(fruit.items()) #
print(fruit) #

