def merge_sort(array, start, mid, end):
    left = start
    right = mid
    temp = []

    while (left < mid and right < end):
        if array[left] < array[right]:
            temp.append(array[left])
            left = left + 1
        else:
            temp.append(array[right])
            right = right + 1

    while (left < mid):
        temp.append(array[left])
        left = left + 1

    while (right < end):
        temp.append(array[right])
        right = right + 1
    #print("left: ", array[start:mid], ", right: ", array[mid:end], ", temp: ", temp)
    for c in range(len(temp)):
        array[start+c] = temp[c]

def divide_and_merge(array, start, end):
    mid = int((start + end)/2)

    if ((start + 1) < end):
        divide_and_merge(array, start, mid)
        divide_and_merge(array, mid, end)

        merge_sort(array, start, mid, end)

array = [1, 4, 9, 0, 8, 2, 6, 3, 7, 5]

print ("Un-Sorted array is:", array)

divide_and_merge(array, 0, len(array))

print ("Sorted array is:", array)
