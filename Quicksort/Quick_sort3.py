
with open('QuickSort.txt','r') as f:
    array = []
    for line in f:
        array.append(int(line.strip()))



def qsort(arr,start,end):

    ## Base case:
    if start >= end: return 0

    res = end-start-1
    i  = start
    j  = i+1

    ## 建立两个指针，i指针指向小于pivot number的集合末尾，j指针指向还没有和pivot number比较的下一个数。
    ## 思路是最后用i指针切割小于pivot number的集合和大于pivot number的集合，让pivot number和i位置调换。 实现两个集合被pivot number分隔
    ## 所以在比较过程中，
    ## 如果发现下一个数大于pivot number，就j= j+1，i指针不动。因为i指针是记录小于pivot number集合的末尾的指针
    ## 如果发现下一个数小于pivot number，还要比较一下，这个数的前一个数（j-1)位置，是不是大于pivot number. 如果大于，则要将(i+1)位置的数和此数（j位置）
    ## 进行交换。并且i=i+1， 扩展小于pivot number 的集合的末尾。
    ## 最后分两段递归，第一段截取 start 到 i位置 （为什么要包括i），因为函数接受end变量是要代表这个函数的长度，而不是索引值，所以输入的数要正确反应数组的长度，
    ## 如果是i-1，实际上截取的长度会小一个单位。
    ## 第二段截取i+1 到 end 位置
    swap(arr,start,end-1)
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


li = [5,4,32,2,6,3]
x = qsort(array,0,len(array))
print(x)
