class_file = open("class.txt", "w", encoding="utf8")
class_file.write("초록반 5세 5명 파랑반 6세 18명 노랑반 7세 22명")
class_file.close()

read_file = open("class.txt", "r", encoding="utf8")
read = read_file.read()
read_txt = read.split()

for i in range(0, len(read_txt)):
    print(read_txt[i], end=" ")
    if read_txt[i].endswith("명"):
        print()

read_file.close()