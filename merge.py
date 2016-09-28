#!/usr/bin/python
import sys

def merge(nums, frist, middle, last):
    ''' merge '''
    #切片边界，左闭右开并且是以0位开始
    lnums = nums[first:middle+1]
    rnums = nums[middle+1:last+1]
    lnums.append(sys.maxint)
    rnums.append(sys.maxint)
    l = 0
    r = 0
    for i in range(first, last+1):
        if lnums[l] < rnums[r]:
            nums[i] = lnums[l]
            l += 1
        else:
            nums[i] = rnums[r]
            r += 1
            
def merge_sort(nums, first, last):
    '''
    merge sort函数中传递的是下标，不是元素个数
    '''
    if first < last:
        middle = (first + last)/2
        merge_sort(nums, first, middle)
        merge_sort(nums, middle+1, last)
        merge(nums, first, middle, laste)
        
if __name__ == '__main__':
    nums = [1, 4, 20, -5, 4, 7]
    print 'nums is :', nums
    merge_sort(nums, 0, 7)
    print 'merge sort:', nums
