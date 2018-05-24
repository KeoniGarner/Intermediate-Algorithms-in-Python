def selection_sort(arr):
    for i in range(0, len(arr)):
        minimum = arr[i]
        index = i
        for idx in range(i, len(arr)):
            if arr[idx] < minimum:
                minimum = arr[idx]
                index = idx
        temp = arr[i]
        arr[i] = minimum
        arr[index] = temp
    return arr

print selection_sort([1,4,2,5,2,3,6,7,3,6])