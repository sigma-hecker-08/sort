def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while temp < lst[j] and j >= 0:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst

# test
l = [9 ,7 ,5, 6, 4, 5, 3, 2, 3]
print(bubble_sort(l))
