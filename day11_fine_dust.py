def get_air_quality(status: int) -> str:
    if status <= 30:
        # print("좋음") # return 문이 없어 암시적으로 None 출력
        return "좋음"
    elif status <= 80:
        # print("보통")
        return "보통"
    elif status <= 150:
        # print("나쁨")
        return "나쁨"
    else:
        # print("매우 나쁨")
        return "매우 나쁨"

print(get_air_quality(15))
print(get_air_quality(85))
