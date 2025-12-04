def bubbleSort(arr):
    n = len(arr)

    # Function to print array with ( ) only on compared indices
    def format_with_bubble(arr, idx1, idx2):
        formatted = []
        for i in range(len(arr)):
            if i == idx1 or i == idx2:
                formatted.append(f'({arr[i]})')
            else:
                formatted.append(str(arr[i]))
        return ', '.join(formatted)

    print("Original array:", ', '.join(str(x) for x in arr))

    for i in range(n - 1):
        swapped = False
        print(f"\nStep {i + 1}:")
        
        for j in range(0, n - i - 1):
            # Show comparison
            print(format_with_bubble(arr, j, j + 1))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    print("\nSorted array:", ', '.join(str(x) for x in arr))


# Start with your custom array
arr = [64, 24, 25, 12, 22, 11, 90]
bubbleSort(arr)
