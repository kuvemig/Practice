# 거스름돈 계산

def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000
    ten_count = (change % 50000) // 10000
    five_count = (change % 10000) // 5000
    one_count = (change % 5000) // 1000

    print(f"50000원 지폐: {fifty_count}장")
    print(f"10000원 지폐: {ten_count}장")
    print(f"5000원 지폐: {five_count}장")
    print(f"1000원 지폐: {one_count}장")


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)