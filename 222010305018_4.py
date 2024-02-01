def generate_kth_row(k):
    if k < 0:
        return []
    row = [1]
    for i in range(1, k + 1):
        new_element = row[i - 1] * (k - i + 1) // i
        row.append(new_element)
    return row
k = int(input("Enter the index k: "))
result = generate_kth_row(k)
print(f"The {k}th row of Pascal's Triangle: {result}")
