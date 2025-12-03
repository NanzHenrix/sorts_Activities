# Python program for implementation of Insertion Sort

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


        left = ""
        for k in range(i):
            left += str(arr[k])
            if k < i - 1:
                left += ","
        right = ""
        for k in range(i, len(arr)):
            right += str(arr[k])
            if k < len(arr) - 1:
                right += ","

        print(f"Array {i}=[{left}|,{right}]")

# Driver code to test above
arr = [12, 11, 13, 5, 6]

print("Original array:", arr)
insertionSort(arr)
print("\nSorted array is:")
print(arr)


