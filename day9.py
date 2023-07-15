# 반복문
index = 1
# while True:
order = ["아이스 아메리카노", "아이스 카페라떼", "자바칩 프라푸치노"]
for menu in order:
    print(str(index) + "번째 손님")
    print(f"주문하신 {menu} 나왔습니다~")
    index += 1
# countinue : 실행 안하고 다음 반복 대상으로 넘어갈 때
# break : 가장 가까운 반복문 종료

# 리스트 컴프리헨션
# 동작 for 변수 in 반복대상

student = [1, 2, 3, 4, 5]
print(student)
student = [x+1 for x in student]
print(student)
