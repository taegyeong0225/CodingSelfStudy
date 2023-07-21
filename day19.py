import day19_module as a
# from 모듈명 import 함수(기능)명

a.price(3)
a.price_morning(5)
a.price_soldier(6)


#############################

import travel.thailand # 패키지.모듈, 함수나 클래스는 못 가져옴 (import문만 단독 사용시)

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

#############################

from travel.thailand import ThailandPackage

trip_to = ThailandPackage()
trip_to.detail()

#############################

from travel import vietnam

trip_to = vietnam.VietnamPackage() #  vietnam이라는 모듈의 클래스의 인스턴스를 trip_to에 할당
trip_to.detail()

#############################

from travel import * # __all__ = ["vietnam"]

trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

#############################

import inspect # 모듈 위치 확인
from travel import *
import math

print(inspect.getmodule(thailand))
print(inspect.getmodule(math))

#############################

import inspect
from day19_greeting import *

print(inspect.signature(greet))

import random

print(inspect.getfile(random))