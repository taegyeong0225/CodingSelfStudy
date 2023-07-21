def profile(name : str, age : int, main_lang : str): # 매개변수
    global fruit # 전역변수 선언
    fruit = "사과"
    print(fruit)
    number = 3 # 지역변수 선언 및 대입
    print(number)
    print(name, age, main_lang)


profile("믹영", main_lang="python", age=17)  # 일반 전달값 -> 키워드 인자
print(fruit)

# print(number) 지역변수이므로 오류
