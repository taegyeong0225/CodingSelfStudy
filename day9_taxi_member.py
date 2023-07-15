# 택시 승객 수 구하기
from random import randrange

index = 1
count = 0
while index <= 50:
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print(f"[0] {index}번째 손님 (소요시간 : {time})")
        count += 1
        index += 1
    else:
        print(f"[ ] {index}번째 손님 (소요시간 : {time})")
        index += 1
print(f"총 탑승객 : {count}명")
