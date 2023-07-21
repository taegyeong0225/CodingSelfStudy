class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛을 생성했습니다.")

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다 (속도 : {self.speed})")

    def damaged(self, damage):
        print(f"{self.name} : {damage}만큼의 피해를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력 {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        super().__init__(name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향 적군을 공격합니다. 공격력 {self.damage}")

    def damaged(self, damage):
        print(f"{self.name} : {damage}만큼의 피해를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력 {self.hp}")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

class Soldier(AttackUnit):
    def __init__(self):
        super().__init__("보병", 40, 5, 1)

    def booster(self):
        if self.hp > 10:
            self.hp -= 10  # 체력 10 소모
            print(f"{self.name} : 강화제를 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족해 기술을 사용할 수 없습니다")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 : {self.flying_speed}]")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        super().__init__(name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

class BuildingUnit(Unit):  # 단일 상속
    def __init__(self, name, hp, damage, location):
        super().__init__(name, hp, damage)
        self.location = location

class Tank(AttackUnit):
    siege_developed = False

    def __init__(self):
        super().__init__("탱크", 150, 35, 1)
        self.siege_mode = False

    # 시지 모드 설정
    def set_siege_mode(self):
        if not Tank.siege_developed:
            return

        if not self.siege_mode:
            print(f"{self.name} : 시지 모드로 전환합니다.")
            self.damage *= 2
            self.siege_mode = True
        else:
            print(f"{self.name} : 시지 모드를 해제합니다.")
            self.damage //= 2
            self.siege_mode = False

class FlyableUnit(Flyable, Unit):
    def __init__(self, flying_speed):
        super().__init__(self, flying_speed)

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

class Stealth(FlyableAttackUnit):
    def __init__(self):
        super().__init__("전투기", 80, 20, 5)
        self.cloaked = False

    def cloaking(self):
        if self.cloaked:
            print(f"{self.name} : 은폐 모드를 해제합니다.")
            self.cloaked = False
        else:
            print(f"{self.name} : 은폐 모드를 설정합니다.")
            self.cloaked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : Good Game")
    print("[Player] 님이 게임에서 퇴장했습니다.")

if __name__ == "__main__":
    game_start()

    so1 = Soldier()
    so2 = Soldier()

    ta1 = Tank()
    ta2 = Tank()

    attack_units = [so1, so2, ta1]

    for unit in attack_units:
        unit.move("1시")

    marine = Unit("마린", 40, 40)
    stealth = Unit("전투기", 80, 50)
    stealth.cloaked = True
    if stealth.cloaked:
        print(f"{stealth.name}는 현재 클로킹 상태입니다.")

    marine = AttackUnit("Marine", 40, 5, 50)
    print(isinstance(marine, AttackUnit))

    game_over()
