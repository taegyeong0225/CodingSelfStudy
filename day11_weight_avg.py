def std_weight(height, gender):
    if gender == "여자":
        avg_weight = (height / 100) ** 2 * 21
    if gender == "남자":
        avg_weight = (height / 100) ** 2 * 22
    print(f"키 {height}cm 남자의 표준 체중은 {avg_weight:.2f}kg입니다.")


std_weight(175, "남자")
