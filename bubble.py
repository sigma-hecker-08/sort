def bubble_sort(l):
    for _ in range(1, len(l)):
        for i in range(1, len(l)):
            if l[i] > l[i-1]:
                l[i], l[i-1] = l[i-1], l[i]
    return(l)

# test
l = [9 ,7 ,5, 6, 4, 5, 3, 2, 3]
print(bubble_sort(l))
