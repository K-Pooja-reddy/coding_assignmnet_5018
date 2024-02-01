def is_prime(N):
    if N < 2:
        return 0
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return 0
    return 1
user_input = int(input("Enter a number: "))
result = is_prime(user_input)
print("Output:", result)