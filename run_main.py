
def quick_sort(list):

    for i in range(0,len(list)):
        for j in (i+1,len(list)):
            if list[i]==list[j]:
                list.pop(i) and list.pop(j)
                return list




print(quick_sort([1,23,4,2,33,33,1]))