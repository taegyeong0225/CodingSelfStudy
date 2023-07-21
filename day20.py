name = "jin"
print(dir(name)) # 메서드 확인 가능

#########################################

import glob
print(glob.glob("./travel/*.py"))

#########################################

import os
folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제했습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했습니다.")

#########################################

import datetime
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td, "입니다.")

#########################################

import datetime
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리는 100일 전", today - td, "에 만났습니다.")

#########################################

import datetime
today = "2023-03-17"
date = datetime.datetime.strptime(today, "%Y-%m-%d").date()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", date + td, "입니다.")
