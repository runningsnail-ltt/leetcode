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
    """
    如果将数组中所有数字用异或符号连接起来，
    则出现偶数次的数字失效，最终结果为出现奇数次的数字的异或。
    """
    def singleNumber3(self,nums):
        result = 0
        for num in nums:
            result = result ^ num
            # print result,num
        return result

    def rotate(self, nums, k):
        """
        # python slice
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] = nums[length-k:]+nums[:length-k]
        return nums

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        result=[]
        i=0
        j=0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] <nums2[j]:
                i +=1
            else:
                j+=1
        return result

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        n = len(nums)
        for x in range(n):
            a = target - nums[x]
            if nums[x] in dic:
                return dic[nums[x]],x
            else:
                dic[a]=x

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profix = 0

        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profix += prices[i+1]-prices[i]
        return profix

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flg = 0
        x = Counter(nums)
        for k,v in x.items():
            if v > 1:
               flg=1
        if flg == 1:
            return True
        else:
            return False

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums = int(''.join(map(str,digits)))+1
        digits = [int(x) for x in str(nums)]
        return digits

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # count = nums.count(0)
        # for i in range(count):
        #     nums.remove(0)
        # nums.extend(count*[0])
        # return nums
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)
        return nums

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    for column in range(9):
                        if column != j and board[i][j] == board[i][column]:
                            return False
                    for row in range(9):
                        if row != i and board[i][j] == board[row][j]:
                            return False
                    for row in range((i//3)*3,(i//3)*3 +3):
                        for column in range((j//3)*3,(j//3)*3 + 3):
                            if row != i and column != j and board[row][column] == board[i][j]:
                                return False
        return True

    def rotate(self, matrix):
        """
        # 先把矩阵转置一下然后翻转，矩阵是以list的list存储，以行为单位，行之间的操作要比列要简单
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list,zip(*matrix[::-1]))
        return matrix
if __name__ == '__main__':
    matrix =[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print Solution().rotate(matrix)


