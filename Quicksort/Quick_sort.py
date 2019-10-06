

with open('QuickSort.txt','r') as f:
    array = []
    for line in f:
        array.append(int(line.strip()))

com_num = 0

def qsort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]

    left = [x for x in arr if x <pivot]
    middle = [x for x in arr if x ==pivot]
    right = [x for x in arr if x> pivot]

    total_com = len(left)+len(right)-1

    global com_num
    com_num += total_com
    return qsort(left)+qsort(middle)+qsort(right)

sort_array = qsort(array)
print(sort_array)
print(com_num)
