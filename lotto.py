# 오늘의 당첨번호 _ 로또

import random
import time

count = int(input("로또를 몇 개 구매하시겠습니까? "))

for i in range(count):
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    print(lotto)

print("두근두근")
time.sleep(2)

for i in range(count):
    bonus = random.sample(range(1, 46), 1)
    print(bonus)

print("Good Luck!!")