def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        curr = a_list[i]
        position = i

        while position > 0 and curr < a_list[position-1]:
            a_list[position] = a_list[position - 1]
            position -= 1
        a_list[position] = curr
    return a_list

print (insertion_sort([1,4,2,5,2,3,6,7,3,6]))