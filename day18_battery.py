# 350p 배터리 관리

class BatteryError(Exception):
    def __init__(self):
        print("배터리가 부족해 스마트폰을 종료합니다.")

def save_battery(level : int) -> None:
    try:
        print(f"배터리 잔량 : {level}%")
        if level > 30:
            status = "일반 모드"
        elif 5 < level <= 30:
            status = "절전 모드"
        else:
            raise BatteryError
    except BatteryError:
        pass


save_battery(75)
save_battery(20)
save_battery(3)
