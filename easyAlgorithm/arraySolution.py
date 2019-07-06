# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter

class Solution(object):

    def removeDuplicates(self, nums):
        """
        # 在排序数组中删除重复项
        # time()
        # space(o(1))
        :param nums: List(int)
        :return: int
        """
        if len(nums)<1:
            return 0
        else:
            last = nums[-1]
            for i in range(len(nums)-2,-1,-1):
                if nums[i] == last:
                    del nums[i]
                else:
                    last = nums[i]
            return len(nums)
    def singleNumber1(self, nums):
        """
        # 只出现一次的数字
        :param nums: List(int)
        :return: int
        """
        x = [a for a in nums if nums.count(a)==1]
        return x[0]
    def singleNumber2(self,nums):
        x = Counter(nums)
        for k,value in x.items():
            if value < 2:
                return k
    def singleNumber3(self,nums):
        result = 0
        for num in nums:
            result = result ^ num
            # print result,num
        return result

if __name__ == '__main__':
    nums=[1,1,3,2,3]
    print Solution().singleNumber3(nums)