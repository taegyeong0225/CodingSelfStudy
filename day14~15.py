class Unit:
    def __init__(self, name: str, hp: int) -> None:  # 생성자
        # 매개 변수 3개, 인스턴스 변수 4개
        self.name = name
        self.hp = hp
        print(f"{self.name} 유닛이 생성됐다.")
        self.cloaking = False
        print(f"체력 {self.hp}")  # 공격력 {self.damage}")
        # 생성자 오버로딩 지원 안 함! (하나의 클래스에 하나의 생성자) != java

    # 메소드 생성
    def __initMessage(self):
        print(f"{self.name} 유닛이 생성됐다.")
        # print(f"체력 {self.hp}, 공격력 {self.damage}")

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다")

class Unit2:
    def __init__(self, name: str, hp: int) -> None:  # 생성자
        # 매개 변수 3개, 인스턴스 변수 4개
        self.name = name
        self.hp = hp
    def sayHi(self):
        print("HELLO")

class AttackUnit(Unit2, Unit):
    def __init__(self, name: str, hp: int, damage: int) -> None:
        # 부모 클래스의 생성자 호출
        super().__init__(name, hp)
        self.damage = damage

class Flyable:
    def __init__(self, flying_speed) -> None:
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name: str, hp: int, damage: int, flying_speed) -> None:
        # 부모 클래스의 생성자 호출
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다")


class Building_Unit(Unit): # 단일 상속
    def __init__(self, name, hp, location):
        super().__init__(name, hp)
        self.location = location


class Flyable_Unit(Flyable, Unit): # 다중 상속
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)


def game_start():
    pass # 동작없이 넘어가기

def game_over():
    pass

game_start()

# 객체(클래스의 인스턴스) 생성
marine = Unit("마린", 40)
stealth = Unit("전투기", 80)
stealth.cloaking = True
if stealth.cloaking is True:
    print(f"{stealth.name}는 현재 클로킹 상태입니다.")

marine = AttackUnit("Marine", 40, 5)
print(isinstance(marine, Unit))
# 마린은 유닛의 인스턴스인가?

game_over()


