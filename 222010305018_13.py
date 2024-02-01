def convert_to_title(A):
    result = ""
    while A > 0:
        A -= 1
        remainder = A % 26
        char = chr(ord('A') + remainder)
        result = char + result
        A //= 26
    return result
user_input = int(input("Enter a positive integer: "))
result = convert_to_title(user_input)
print("Output:", result)
