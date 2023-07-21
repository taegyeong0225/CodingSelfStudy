class ParkingManagaer:
    def __init__(self, capacity):
        self.capacity = capacity  # 조건 1
        print(f"총 {capacity}대를 등록할 수 있습니다.")
        self.count = 0

    def register(self):
        self.count += 1
        if self.count > self.capacity:
            print("더 이상 등록할 수 없습니다.")
            return
        print(f"차량 신규 등록 ({self.count}/{self.capacity})")


manager = ParkingManagaer(5)
for i in range(6):
    manager.register()
