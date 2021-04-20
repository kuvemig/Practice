#피보나치 수열

def fibo(n):
    return fibo(n-1) + fibo(n-2) if n >= 2 else n

for n in range(1, 9):
    print(n, fibo(n))

# 트럼프 카드

i = 1
while i <= 52:
    for j in ["spade", "heart", "diamond", "clover"]:
        for k in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]:

            print(i,j,k)
            i += 1

