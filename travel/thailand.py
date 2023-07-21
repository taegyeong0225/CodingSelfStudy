class ThailandPackage:
    def detail(self):
        print("[태국 3박 5일 패키지] 방콕, 파타야 여행(야시장 투어) 50만 원")

if __name__ == "__main__": # __name__은 내장변수 (모듈 이름과 같음, 역할이 이미 정의된 변수)
    print("thailand 모듈을 직접 실행")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("thailand 외부에서 모듈 호출")