def min_candies(A):
    n = len(A)
    candies = [1] * n
    for i in range(1, n):
        if A[i] > A[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if A[i] > A[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)
A = list(map(int, input("Enter the ratings of children separated by space: ").split()))
output = min_candies(A)
print("Minimum candies required:", output)