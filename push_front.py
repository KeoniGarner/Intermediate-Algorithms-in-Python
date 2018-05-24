def push_front(arr, val):
    arr.append(arr[len(arr) - 1])
    for index in range(len(arr)-1, 0, -1):
        arr[index] = arr[index-1]
    arr[0] = val
    return arr

print push_front([1,2,3,6,5,23,2,5,25,2,52,52,6], 18)