def find_intersection(A, B):
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return result
A = list(map(int, input("Enter the elements of sorted array A (space-separated): ").split()))
B = list(map(int, input("Enter the elements of sorted array B (space-separated): ").split()))
intersection_result = find_intersection(A, B)
print("Output:", intersection_result)
