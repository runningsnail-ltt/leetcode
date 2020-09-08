# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxsum = float("-inf")

        def Gain(root):
            if not root:
                return 0
            leftGain = max(Gain(root.left), 0)
            rightGain = max(Gain(root.right), 0)
            pricesum = leftGain + rightGain + root.val

            self.maxsum = max(self.maxsum, pricesum)
            return max(leftGain, rightGain) + root.val

        Gain(root)
        return self.maxsum
    def binarySearch(self,nums,x):
        n = len(nums)
        if n < 1:
            return -1
        start = 0
        end = n-1
        while(start<=end):
            mid = start + (end-start)/2
            if x == nums[mid]:
                return mid
            elif x> nums[mid]:
                start = mid+1
            else:
                end = mid-1
        return -1

    def search(self, nums,target):
        if len(nums) == 0: return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]: return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1




nums = [1,2,3,4,5,6]
print Solution().binarySearch(nums,5)
