# 함수 정의 하기
from typing import Tuple

def open_account():
    print("새로운 계좌를 개설합니다.")

open_account()

def deposit(balance: int, money: int) -> int:
    print(f"{money}원을 입금했습니다. 잔액은{balance + money}원입니다.")
    return balance + money


def withdraw(balance: int, money: int) -> int:
    if balance >= money:
        print(f"{money}원을 출금했습니다.")
        return balance - money
    else:
        print(f"잔액이 부족합니다. 잔액은 {balance}원입니다.")
        return balance


def withdraw_night(balance: int, money: int) -> tuple[int, int]:
    commission = 100
    print(f"업무 시간 외에 {money}원을 출금했습니다.")
    return commission, balance - money - commission