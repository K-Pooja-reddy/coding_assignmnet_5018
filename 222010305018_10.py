def is_palindrome(num):
    if num < 0:
        return 0
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return 1 if original_num == reversed_num else 0
num = int(input("Enter an integer: "))
result = is_palindrome(num)
print("Is palindrome:", result)
