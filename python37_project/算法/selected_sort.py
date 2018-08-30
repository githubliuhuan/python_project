# 直接选择排序
# 时间复杂度O(n^2) 总的比较次数n*(n-1)/2

def selected_sort(lists):
    length = len(lists)
    for i in range(length-1):
        smallest = i
        for j in range(i+1,length-1):
            if lists[j] < lists[smallest]:
                lists[j],lists[smallest] = lists[smallest],lists[j]
    return lists
print(selected_sort([1,4,5,0,6]))