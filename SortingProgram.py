# Quick Sort
# Time Complexity O(n log n)

# Example Inputs
# 5 4 3 2 1
# 1 8 4 7 2 2 0 9 4
# 
# (null)
# 1
# 1 0
# 1 2 3 4 5 6


def QuickSort(arr):
    # Base Case
    if len(arr) < 2:
        return arr

    # The pivot is set as the last element in the list
    pivot_index = len(arr) - 1
    i = 0
    while i < pivot_index:
        while(arr[i] > arr[pivot_index]):
            # For numbers greater or equal to the pivot, 
            # Move them to the right of the pivot
            arr.append(arr[i])
            arr.pop(i)
            pivot_index -= 1
        i += 1

    # Recursion for both left and right sides
    if pivot_index > 0:
        arr[:pivot_index] = QuickSort(arr[:pivot_index])

    if pivot_index < len(arr) - 1:
        arr[pivot_index + 1:] = QuickSort(arr[pivot_index + 1:])

    # Return the sorted array
    return arr


def main():
    arr = [int(i) for i in input().split()]
    print(QuickSort(arr))

main()
