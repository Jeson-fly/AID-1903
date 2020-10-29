import random


# 冒泡排序  时间复杂度o(n²)
def maopao_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
        print("冒泡排序：", li)


# 选择排序   时间复杂度o(n²)
def choice_sort(li):
    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
        print("选择排序：", li)


# 插入排序    时间复杂度o(n²)
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while li[j] > tmp and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print("插入排序:", li)


# 快速排序   时间复杂度o(nlog（n）)
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while li[right] >= tmp and left < right:
            right -= 1
        li[left] = li[right]
        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    # print("快速排序：",li,left)
    return left

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

li = list(range(10))
random.shuffle(li)
print(li)
maopao_sort(li)
print("-" * 50)
random.shuffle(li)
print(li)
choice_sort(li)
print("-" * 50)
random.shuffle(li)
print(li)
insert_sort(li)
print("-" * 50)

li = list(range(10000))
random.shuffle(li)
print(li)
# partition(li,0,len(li)-1)
quick_sort(li,0,len(li)-1)
print(li)