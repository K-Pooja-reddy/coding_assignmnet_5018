def add_one(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        current_sum = digits[i] + carry
        digits[i] = current_sum % 10
        carry = current_sum // 10
    if carry:
        digits.insert(0, carry)
    return digits
digits_input = list(map(int, input("Enter the array of digits separated by space: ").split()))
result = add_one(digits_input)
print("After adding one:", result)
