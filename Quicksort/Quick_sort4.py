
with open('QuickSort.txt','r') as f:
    array = []
    for line in f:
        array.append(int(line.strip()))



def qsort(arr,start,end):
    ## Base case:
    if start >= end: return 0
    middle = choose_middle(end,start)
    choice_list = [arr[start],arr[end-1],arr[middle]]
    index = proper_index(choice_list,start,end,middle)
    # print(arr[index],start,end)
    swap(arr,start,index)

    res = end-start-1
    i  = start
    j  = i+1
    while j <end:
        if arr[start]>arr[j]:
            if arr[start]<arr[j-1]:swap(arr,i+1,j)
            i+=1
        j+=1
    swap(arr,start,i)
    res +=qsort(arr,start,i)
    res +=qsort(arr,i+1,end)

    return res

def swap(arr,fir,sec):
    temp = arr[sec]
    arr[sec]=arr[fir]
    arr[fir] = temp


def median(x,i,j,k):

    if (x[i]-x[j])*(x[i]-x[k]) < 0:
        return i
    elif (x[j]-x[i])*(x[j]-x[k]) < 0:
        return j
    else:
        return k



def choose_middle(end,start):
    # if (end-start)%2 == 0:
    #     middle = (start + (end-start)//2)-1
    # else:
    #     middle = start + ((end-start)+1)//2-1
    middle = start + (end-start-1)//2
    return middle


def proper_index(choice_list,start,end,middle):
    if  median(choice_list,0,1,2)==0:
        return start
    elif median(choice_list,0,1,2)==1:
        return end-1
    else:
        return middle



li = [5,4,32,2,6,3,1,23]
x = qsort(array,0,len(array))
print(x)
