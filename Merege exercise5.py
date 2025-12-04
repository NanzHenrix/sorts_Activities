splits = []

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    splits.append((arr, leftHalf, rightHalf))

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    merged = merge(sortedLeft, sortedRight)
    return merged

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsortedArr = [3, 7, 6, 10, 15, 23.5, 55, -13]
print("Original array:", unsortedArr)

# Perform mergeSort, but only print splits first
sortedArr = mergeSort(unsortedArr)

# Print all splits at once
print("\nAll splitting steps:")
for full, left, right in splits:
    print(f"Split {full} into {left} and {right}")

# Now print merging steps by re-sorting but this time print merges
def mergeSortWithMerging(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSortWithMerging(leftHalf)
    sortedRight = mergeSortWithMerging(rightHalf)

    merged = merge(sortedLeft, sortedRight)
    print(f"Merged {sortedLeft} and {sortedRight} => {merged}")
    return merged

print("\nMerging steps:")
mergeSortWithMerging(unsortedArr)

print("\nSorted array:", sortedArr)
