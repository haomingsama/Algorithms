
with open('QuickSort.txt','r') as f:
    array = []
    for line in f:
        array.append(int(line.strip()))



def qsort(arr,start,end):
    '''
    This function count the number of comparsion during quick sort process

    Parameters
    ------------
    arr : list
        Array to sort

    start: int
    staring point of the array.

    end: int
    the length of the array

    Returns
    -------------
    number of comparison: int

    Usage
    -------------
    qsort(arr,start,end) >> number of comparison during the quick sort

    '''
    ## Base case: 当数组长度剩下一个的时候，直接返回0，不做比较
    if start >= end: return 0
    '''
    下面这一段目的是，
    在每次迭代中选出头部，尾部和中部的数据，组成一个新的数组，取其中的中位数，然后将此数作为pivot number
    并且用index来确定其value。与头部数据交换。
    '''
    middle = choose_middle(end,start)
    choice_list = [arr[start],arr[end-1],arr[middle]]
    index = proper_index(choice_list,start,end,middle) #这里返回的是中位数在原数组的index，
    # print(arr[index],start,end)
    swap(arr,start,index) # 根据两个index来交换数据



    '''
    思路是最后用i指针切割小于pivot number的集合和大于pivot number的集合，让pivot number和i位置调换。 实现两个集合被pivot number分隔
    所以在比较过程中，
    如果发现下一个数大于pivot number，就j= j+1，i指针不动。因为i指针是记录小于pivot number集合的末尾的指针
    如果发现下一个数小于pivot number，还要比较一下，这个数的前一个数（j-1)位置，是不是大于pivot number. 如果大于，则要将(i+1)位置的数和此数（j位置）
    进行交换。并且i=i+1， 扩展小于pivot number 的集合的末尾。
    最后分两段递归，第一段截取 start 到 i位置 （为什么要包括i），因为函数接受end变量是要代表这个函数的长度，而不是索引值，所以输入的数要正确反应数组的长度，
    如果是i-1，实际上截取的长度会小一个单位。
    第二段截取i+1 到 end 位置
    '''
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
    '''
    Given arr and index, swap the value of this two position

    Parameters
    -----------
    arr: list
    arr that is input to be swapped

    fir: int
    the index of the first element to be swapped

    sec: int
    the index of the second element to be swapped

    Returns
    ----------
    No return， once the function complete swapping, the function ends

    Usage
    ----------
    swap(arr,fir,sec) >> arr is swapped in the fir and sec position
    '''
    temp = arr[sec]
    arr[sec]=arr[fir]
    arr[fir] = temp


def median(x,i,j,k):
    '''
    Given arr(x) and index(i,j,k), find the median value of the three number.

    Rationale
    -----------
    Utilize the fact that the median is smaller than the max but is larger than the min
    so we have (median - min)*(median-max) < 0. Using this equation to help us find the median among the three numbers
    Which index satisfy the inequality, we choose it as our median value index

    Parameters
    -----------
    x: list
    x is the array

    i,j,k: int
    index number of the three value

    Returns
    ----------
    index: return the index (one of the i,j,k) represent the median value position in the array

    Usage
    ----------
    median(arr,0,1,2) >> one of the index(0/1/2) that represent the medium value in the list
    '''
    if (x[i]-x[j])*(x[i]-x[k]) < 0:
        return i
    elif (x[j]-x[i])*(x[j]-x[k]) < 0:
        return j
    else:
        return k



def choose_middle(end,start):
    '''
    Given a list with the length of k, find the middle point of the list

    Rationale
    -----------
    If the list has 2k element, the middle point should be the kth element
    if the list has 2k+1 element, the middle point should be the (2k+1)-1/2 th element
    This two rule can be expressed as start + (m-1)//2 (向下取整) while m is the total length of the list

    Parameters
    -----------
    end: int
    total len of the list


    start: int
    starting point of the list

    Returns
    ----------
    middel: the middle index of the array

    Usage
    ----------
    choose_middle(end,start) >> the index of the middle point. arr[middle] represent the middle point value
    '''

    middle = start + (end-start-1)//2
    return middle


def proper_index(choice_list,start,end,middle):
    '''
    Output the right corresponding index in the array according to the result of median function

    Rationale
    -----------
    Map the index in median function(0,1,2) to the actual array index (start, middle, end)


    Parameters
    -----------
    choice_list: list
    list that contain three number(start,end, middle point value)


    start: int
    starting point of the list

    end : int
    the end point of the list

    middel : int
    the middle point of the list

    Returns
    ----------
    actual index of the array

    Usage
    ----------
    proper_index(choice_list, star, end,middle) >> the index represent the middle index in the array
    '''

    if  median(choice_list,0,1,2)==0:
        return start
    elif median(choice_list,0,1,2)==1:
        return end-1
    else:
        return middle



li = [5,4,32,2,6,3,1,23]
x = qsort(array,0,len(array))
print(x)
