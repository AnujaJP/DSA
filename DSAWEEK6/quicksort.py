def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = []
    for x in arr:
        if x < pivot:
            left.append(x)

    right = []
    for x in arr:
        if x > pivot:
            right.append(x)

    middle = []
    for x in arr:
        if x == pivot:
            middle.append(x)

    return quicksort(left) + middle + quicksort(right)


arr = [10, 7, 8, 9, 1, 5]
print(quicksort(arr))
