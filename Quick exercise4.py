def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    print(f"\nPartitioning with pivot [{pivot}] between indexes {low} and {high}")
    print("Before partition:", ', '.join(str(x) for x in arr))

    for j in range(low, high):
        # Show the comparison with [ ] on compared elements
        compared = [f"[{arr[x]}]" if x == j or x == high else str(arr[x]) for x in range(len(arr))]
        print("Comparing:", ', '.join(compared))

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # Show the swap with [ ] around swapped elements
            swapped = [f"[{arr[x]}]" if x == i or x == j else str(arr[x]) for x in range(len(arr))]
            print("Swapped :", ', '.join(swapped))

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    final_swap = [f"[{arr[x]}]" if x == (i+1) or x == high else str(arr[x]) for x in range(len(arr))]
    print("Moved pivot:", ', '.join(final_swap))

    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        print(f"--> Left of pivot [{arr[pi]}]: {arr[low:pi]}")
        print(f"--> Right of pivot [{arr[pi]}]: {arr[pi+1:high+1]}")

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# Driver code
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", ', '.join(str(x) for x in arr))
quickSort(arr, 0, len(arr) - 1)

print("\nSorted array:")
print(', '.join(str(x) for x in arr))
