def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    print('num:'+str(num))
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    print(left,right)
    return Merge(left, right)
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    print(result)
    return result

print(merge_sort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]))