def climbStairs(A):
    if A <= 0:
        return 0
    if A == 1:
        return 1
    if A == 2:
        return 2
    dp = [0] * (A + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, A + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[A]
A = int(input("Enter the number of steps: "))
output = climbStairs(A)
print("Number of distinct ways to climb to the top:", output)
