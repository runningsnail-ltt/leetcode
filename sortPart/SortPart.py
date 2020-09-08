# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter

def QuickSort(list_):
    """
    快速排序：
    :param list_: 
    :return: 
    """
    if len(list_) <=1:
        return list_
    left = []
    right = []
    base = list_.pop()

    for x in list_:
        if x<=base:
            left.append(x)
        else:
            right.append(x)
    return QuickSort(left)+[base]+ QuickSort(right)

def merge(left,right):
    c = []
    i = j = 0
    while (i<len(left) and j < len(right)):
        if left[i] < right[j]:
            c.append(left[i])
            i = i+1
        else:
            c.append(right[j])
            j = j+1
    while(i < len(left)):
        c.append(left[i])
        i = i + 1
    while(j<len(right)):
        c.append(right[j])
        j = j + 1
    return c


def MergeSort(list_):
    if len(list_)<=1:
        return list_
    mid = int(len(list_)/2)
    left = MergeSort(list_[mid:])
    right = MergeSort(list_[:mid])
    return merge(left,right)


def max_heapify(heap,heapSize,root):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
    '''
    给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
    父节点：(root-1)//2
    左子节点：2*root + 1
    右子节点：2*root + 2  即：左子节点 + 1
    '''
    left = 2*root + 1
    right = left + 1
    larger = root
    if left < heapSize and heap[larger] < heap[left]:
        larger = left
    if right < heapSize and heap[larger] < heap[right]:
        larger = right
    if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
        heap[larger], heap[root] = heap[root], heap[larger]
        # 递归的对子树做调整
        max_heapify(heap, heapSize, larger)

def build_max_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    heapSize = len(heap)
    for i in range((heapSize -2)//2,-1,-1):  # 自底向上建堆
        max_heapify(heap, heapSize, i)

def heap_sort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行堆调整过程。
    build_max_heap(heap)
    # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)
    return heap


print MergeSort([2,5,3,4,8,9,10,30,24,25])