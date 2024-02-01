def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
nums_input = list(map(int, input("Enter the array of numbers separated by space: ").split()))
result = majority_element(nums_input)
print("Majority Element:", result)
