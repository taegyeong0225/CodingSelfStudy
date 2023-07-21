# 파일 입출력 (파일 객체)
score_file = open("score.txt", "w", encoding="utf8") # a는 이어쓰기
print("수학 : 100", file=score_file)
score_file.write("국어 : 100\n")
score_file.write("영어 : 100")
score_file.close()

# r : read(), readline() : 한줄씩 출력, readlines() : 모든 내용을 list 형태로 저장
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="") # 한줄씩 출력

# data를 file로 저장 (객체 자체를 저장)
import pickle

profile_file = open("profile.pickle", "wb") # 바이너리 파일로 저장
profile = {"이름":"snoopy", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)

pickle.dump(profile, profile_file) # 덤프로 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # load로 데이터 불러오기
# 이진형태로 저장되어 있어서 print로 출력하면 의도대로 안 나옴
profile = pickle.load(profile_file) 
print(profile)
profile_file.close()

# 파일 한 번에 닫기 with
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
# print(profile_file._checkClosed()) 닫혔는지 확인