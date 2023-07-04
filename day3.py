#연산자
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3) # 결과를 실수로 연산 (파이썬의 자동 형 변환 때문), 자바에서는 몫을 구하는 연산자

print(2 ** 3) # 자바에서는 Math 클래스의 pow()메소드를 사용해야 함
print(10 % 3)
print(10 // 3) # 자바에서의 /
print("---------------")

# 비교연산자
print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)
print(1 != 3)

print((3 > 0) and (3 > 5))
print((3 > 0) or (3 > 5))
print(not(1 != 3))

print(5 > 4 > 3)
print(4 > 5 > 3) # 자바에서는 한 항에 하나의 비교연산자만 가능(& && | || 로 이어서 사용)

print(2 + 3 * 4)
print((2 + 3) * 4)
print("---------------")

# 변수 연산
number = 2 + 3 * 4
print(number) # 14
number = number + 2  # 2 + 3 * 4 + '2'
print(number) # 16

number += 2 # number = number + 2
print(number)
number -= 2 # number = number - 2
print(number)
number *= 2 # number = number * 2
print(number)
number /= 2 # number = number / 2
print(number)
number **= 2 # number = number ** 2
print(number)
number //= 2 # number = number // 2
print(number)
number %= 2 # number = number % 2
print(number)


# 함수
print(abs(-5)) # -5의 절대값
print(pow(4, 2)) # 4를 제곱한 값
print(max(5, 12)) # 5와 12 중 큰 값
print(min(5, 12)) # 5와 12 중 작은 값
print(round(3.14)) # 3.14를 소수점 이하 첫째 자리에서 반올림한 정수
print(round(4.678, 2)) # 4.678을 소수점 이하 셋째 자리에서 반올림한 값


#모듈의 기능 가져다 쓰기
from math import * # math 모듈의 모든 기능

result = floor(4.99)
print(result) # 4.99의 내림
result = ceil(3.14)
print(result) # 3.14의 올림
result = sqrt(16)
print(result) # 16의 제곱근


#모듈 사용
from random import * # random 모듈의 모든 기능을 가져다 쓰겠다는 의미

# random
print(random()) # 0 ~ 9.99999...
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1)
print(int(random() * 45) + 1)
print(randrange(1, 46)) # 1 <= x < 46

# randint
print(randint(1, 45)) # 1 <= x < 45
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))

# 1. 3 + 5 의 실행 결과로 올바른 것은?
#   3번 8
# 2. 6 / 3 의 실행 결과로 올바른 것은?
#   4번 2.0 (정수로 원한다면 6//3)
# 3. 5 % 3 의 실행 결과로 올바른 것은?
#   2번 2
# 4. (5<3) or (7<3)연산의 의미로 올바른 것은?
#   1번 5가 3보다 작거나 7이 3보다 작다.
# 5. 2+3*4에 대해 잘못 설명한 사람은?
#   2번 은하 : (2+3)*4와 결과가 같아 -> 문제는 14, 2번은 20이므로 다르다.
# 6. num = 3; (가) print(num)에서 (가)에 들어갈 코드로 옳은 것은?
#   2번 num *= 2
# 7. print(round(0.1357, 2))의 실행결과
#   4번 0.14
# 8. random 모듈에 대해 잘못 설명한 사람은?
#   2번 은하: random() 함수는 0.0 이상 1.0 이하의 난수를 생성해 -> 0.0 이상 10.0 미만


"""
***정리***
/를  이용한 나눗셈의 결과는 실수
** 거듭제곱, // 몫
"""