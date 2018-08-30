# 冒泡排序
def bubble_sort(lists):
    for i in range(len(lists) - 1):
        print(i)
        for j in range(len(lists) - 1 - i):
            if lists[j] > lists[j + 1]:
                print(lists)
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists

# print('--------')
# print('错误示范')
# def bubble_sortt(lists):
print(bubble_sort([2,1,3,0]))
#     count = len(lists)
#     for i in range(0, count):
#         print(i)
#         for j in range(i + 1, count):
#             if lists[i] > lists[j]:
#                 print(lists)
#                 lists[i], lists[j] = lists[j], lists[i]
#     return lists
# print(bubble_sortt([2,1,3,0]))