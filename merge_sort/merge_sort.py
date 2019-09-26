


def merge_sort(seq):
    #设置递归截止的条件，当只有一个数的时候，就返回本数
    if len(seq)<=1:
        return seq
    mid = int(len(seq)/2) #需要注意python如果不用int的话，出现的是小数，无法进行slicing
    left = merge_sort(seq[:mid]) #运用little schmer 发，在纸上画出每一层会返回的值
    right = merge_sort(seq[mid:])
    return merge(left,right) #注意当所有值返回后，每一层都要进行一个merge 操作




def merge(left,right):
    result = []
    i = 0
    j = 0
    global count #要声明这是调用的全局变量
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1

        else:
            result.append(right[j])
            j+=1
            count = count + (len(left)-i) #只有当右边的数被选中的时候，才能进行逆数组的运算

    result +=left[i:]

    result +=right[j:] #就算j的长度已经超过数组的长度，也会返回[]，利用这一点添加排序后剩下的数字
    return result

### 测试 ####

count = 0 #用来计数有多少对逆数组
li = [] #用来储存读入的数据

with open('IntegerArray.txt','r') as f:
    for line in f:
        li.append(int(line.strip()))#这里要注意读出来的是带有空格的文本数据，要去空格操作以及转换成整数

output = merge_sort(li)

print(output[-5:])
print(count)
