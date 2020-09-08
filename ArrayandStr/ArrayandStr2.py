# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pass


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {"}": "{", "]": "[", ")": "("}

        for char in s:
            if char in mapping:
                topelem = stack.pop() if stack else '#'
                if topelem != mapping[char]:

                    return False
            else:
                stack.append(char)
        return not stack

    def addStrings(self, num1_, num2_):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = [int(x) for x in num1_], [int(x) for x in num2_]
        n1 = len(num1)
        n2 = len(num2)
        i = n1 - 1
        j = n2 - 1
        dump = 0

        res = []
        while (i >= 0 and j >= 0):
            item = (num1[i] + num2[j] + dump) % 10
            dump = (num1[i] + num2[j] + dump) / 10
            res.append(item)
            i -=1
            j -=1
        while (i >= 0):
            item = (num1[i] + dump) % 10
            dump = (num1[i] + dump) / 10
            res.append(item)
            i -=1
        while (j >= 0):
            item = (num2[j] + dump) % 10
            dump = (num2[j] + dump) / 10
            res.append(item)
            j -=1
        if dump == 1:
            res.append(1)
        return "".join(map(str, list(res)[::-1]))

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        for sstr in s.split(" "):
            arr.append(sstr[::-1])
        return " ".join(sstr)

    def merge(self, nums1_, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        nums1 = nums1_[:m]
        nums1_ = []
        while (i < m and j < n):
            if nums1[i] < nums2[j]:
                nums1_.append(nums1[i])
                i += 1
            else:
                nums1_.append(nums2[j])
                j += 1
        if (j < n):
            nums1_.extend(nums2[j:n])
        if (i < m):
            nums1_.extend(nums1[i + 1:m])
        return nums1_

print Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)