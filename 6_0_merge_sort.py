def merge(arr, start, mid, last):
    left = arr[start: mid+1]
    right = arr[mid+1: last+1]

    leftStart = 0
    leftEnd = len(left)
    rightStart = 0
    rightEnd = len(right)
    x = start
    while (leftEnd > 0 and rightEnd > 0 and leftStart < leftEnd and rightStart < rightEnd):
        if left[leftStart] <= right[rightStart]:
            arr[x] = left[leftStart]
            leftStart += 1
        else:
            arr[x] = right[rightStart]
            rightStart += 1
        x+=1

    while (leftStart < leftEnd):
        arr[x] = left[leftStart]
        leftStart += 1
        x += 1
    while (rightStart < rightEnd):
        arr[x] = right[rightStart]
        rightStart += 1
        x += 1

def divide(arr,start, last):
    if start < last:
        mid = ( start + ( last - 1 ) ) //2
        # Sort first and second halves
        divide(arr, start, mid)
        divide(arr, mid + 1, last)
        merge(arr, start, mid, last)

arr = [1, 4, 5, 2, 7, 9, 0, 8, 3, -1]
divide(arr, 0, len(arr) - 1)
print(arr)
