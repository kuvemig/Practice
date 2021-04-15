# 오늘의 당첨번호 _ 연금복권

import random

count = int(input("로또를 몇 개 구매하시겠습니까? "))

for i in range(count):
    lotto = random.sample(range(0, 9), 6)
    print(lotto)

print("Good Luck!!")