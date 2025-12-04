A = [64, 25, 12, 22, 11]
print("Original array:", A)
print("-" * 30)

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[j] < A[min_idx]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
    print(f"Step {i+1}: {A}")
    print("-" * 30)

print("Sorted array:", A)
