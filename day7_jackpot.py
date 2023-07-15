from random import shuffle, sample

list =  []
for i in range(1, 21):
    list.append(i)

shuffle(list)

chicken = sample(list, 1)
coffee = sample(list, 3)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : ", chicken)
print("커피 당첨자 : ", coffee)
print("-- 축하합니다! --")