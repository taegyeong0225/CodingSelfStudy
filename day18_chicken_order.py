# 346p 10.5 치킨 주문하기
chicken = 10
waiting = 1

class SoldOutError(Exception):
    def __init__(self):
        print("재료가 소진되었습니다. 주문이 불가합니다.")

class NumError(Exception):
    def __init__(self):
        pass

while True:
    try:
        print(f"남은 치킨 : {chicken}")
        order = int(input("치킨 몇 마리? "))
        if order > 10:
            raise NumError
            pass
        else:
            if order > chicken:
                print("재료가 부족합니다")
            else:
                print(f"대기 번호 {waiting} - {order}마리 주문하셨습니다.")
                waiting += 1
                chicken -= order
    except ValueError:
        print("값을 잘못 입력했습니다.")
    except NumError:
        print("한 번에 10마리까지 주문 가능합니다")