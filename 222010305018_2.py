def max_profit(A):
    if not A or len(A) == 1:
        return 0
    min_price = A[0]
    max_profit = 0
    for price in A:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
A = list(map(int, input("Enter the stock prices separated by space: ").split()))
output = max_profit(A)
print("Maximum possible profit:", output)
