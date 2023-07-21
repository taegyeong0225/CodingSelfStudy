# 예외 처리
class BigNumberError(Exception): # 사용자 정의 예외 처리, 상속 받음
    def __init__(self, msg): # 객체가 생성되면 자동 호출
        self.msg = msg # 오류 메세지를 받아옴

    def __str__(self): # print() 함수가 객체로 호출되면 함께 호출
        # return self.msg # 오류 메세지 반환
        return "[오류 코드 001]"+ self.msg

def division(num1, num2):
    try:
        # 한 자리 숫자 나누기 전용 계산기
        if num1 >= 10 or num2 >= 10:
            # raise ValueError
            raise BigNumberError(f"입력값 : {num1} / {num2}")
        result = num1 / num2
        print(result)
    except TypeError:
        print("숫자가 아니었음")
    except ZeroDivisionError as m: # 에러 문장을 변수에 받아옴
        print(m)
    except BigNumberError as error:
        print("한 자리수를 입력하세요")
        print(error)
    except Exception as err: # 모든 에러를 다 잡음
        print(err)
    finally: # 무조건 실행
        print("끝\n")

division(3, "삼")
division(3, 0)
division(3, 12)

