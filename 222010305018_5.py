def find_duplicate_and_missing(nums):
    n = len(nums)
    xor_result = 0
    for i in range(1, n + 1):
        xor_result ^= i
        xor_result ^= nums[i - 1]
    rightmost_set_bit = xor_result & -xor_result
    group1 = 0
    group2 = 0
    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            group1 ^= i
        else:
            group2 ^= i

        if nums[i - 1] & rightmost_set_bit:
            group1 ^= nums[i - 1]
        else:
            group2 ^= nums[i - 1]
    for num in nums:
        if num == group1:
            return [group1, group2]
        elif num == group2:
            return [group2, group1]
nums_input = list(map(int, input("Enter the space-separated numbers from 1 to n: ").split()))
result = find_duplicate_and_missing(nums_input)
print("Output:", result)