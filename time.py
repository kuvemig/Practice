# 시간측정
from random import randint
import time
array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()
array.sort()
#프로그램 소스코드

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정 : ", end_time - start_time)