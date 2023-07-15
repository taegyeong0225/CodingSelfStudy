# 슈퍼마켓 2+1 가격 계산
price = 1000
num = 6

for i in range(num):
    print("2+1 상품입니다.")
real_num = num // 3
print(f"총 가격은 {1000 * (num - real_num)}원입니다.")