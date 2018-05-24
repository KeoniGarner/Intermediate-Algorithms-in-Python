def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                print(arr[i], arr[i+1])
                is_sorted = False
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    
    return arr

print bubble_sort([1,4,2,5,2,3,6,7,3,6])