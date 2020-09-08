# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter

class Solution(object):
    def twoSum(self, nums, target):
        """
        两数之和
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        n = len(nums)
        if n < 2:
            return []
        for i in range(0, n):
            if nums[i] in dic:
                return [dic[nums[i]],i]
            else:
                dic[target - nums[i]] = i

    def twoSum(self, nums, target):
        """
        两数之和  有序
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n < 2:
            return []
        i = 0
        j = n - 1
        while (i < j):
            if (nums[i] + nums[j] == target):
                return [i + 1, j + 1]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1



    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def getElem(nums1, n, nums2, m):
            i = 0
            j = 0
            res = []
            while (i < n and j < m):
                if nums1[i] <= nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            if i < n:
                res.extend(nums1[i :])
            if j < m:
                res.extend(nums2[j :])
            return res

        n = len(nums1)
        m = len(nums2)
        res = getElem(nums1, n, nums2, m)
        if (n + m) % 2 == 0:
            return (res[(n + m) / 2] + res[(n + m) / 2 - 1]) / 2.0
        else:
            return res[(n + m - 1) / 2]

    def longestPalindrome(self, s):
        """
        最长回文串，两层循环，注意循环停止的条件
        回文串substr = substr[::-1]
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s
        maxlen = 0
        substr = ""
        maxstr = ""
        for i in range(n):
            if n - i <= maxlen:
                return maxstr
            for j in range(i + maxlen, n + 1):
                substr = s[i:j]
                if substr == substr[::-1]:
                    maxstr = substr
                    maxlen = j - i
        return maxstr

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            k = n - 1
            target = -nums[i]
            for j in range(i + 1, n):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                while (j < k) and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])

        return res

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            return sum(nums)
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            k = n - 1
            j = i +1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s
                if abs(target - s) < abs(target - res):
                    res = s
                if s > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif s < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return res

    def isValid(self, s):
        """
        有效的括号：用栈+字典
        :type s: str
        :rtype: bool
        """
        stack = []
        smap = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in smap:
                topele = stack.pop() if stack else "#"
                if topele != smap[char]:
                    return False
            else:
                stack.append(char)
        return not stack

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        i = 1
        while (i < len(nums)):
            if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)



print Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])