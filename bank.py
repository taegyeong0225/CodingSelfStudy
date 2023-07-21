# 191p

def open_account():
    print("새로운 계좌를 개설합니다")

open_account()

def deposit(balance, money):
    print(f"{money}원 입금, 잔액 {balance + money}")
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print(f"{money}원 출금, 잔액 {balance -  money}")
        return balance - money
    else:
        print(f"잔액이 부족합니다. 잔액은 {balance}입니다.")
        return balance

def withdraw_night(balance: int, money: int) -> tuple[int, int]:
    commission = 100
    print(f"업무 시간 외에 {money}원을 출금했습니다.")
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)

balance = withdraw(balance, 2000)
balance = withdraw(balance, 250)
