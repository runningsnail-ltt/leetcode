# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter

class Solution(object):
    def twoSum(self, numsi, target):
        """
        输入如果是有序的，那最好用双指针，因为不用考虑重复元素的问题如果输入不是有序的，暴力或者结合dic的我认为是比较好的做法
        两数之和比较经典的做法：排序+双指针
        :param nums: 
        :param target: 
        :return: 
        """
        n = len(numsi)

        index1 = 0
        index2 = n-1
        while index1<index2:
            if numsi[index1]+numsi[index2]==target:
                break
            elif numsi[index1]+numsi[index2]> target:
                index2 -= 1
            else:
                index1 +=1

        return [index1, index2]

    def twoSum2(self,nums,target):
        """
        对于无序的，最好的我认为是用dic的方式
        :param nums: 
        :param target: 
        :return: 
        """
        dic = {}
        n = len(nums)
        for x in range(n):
            a = target - nums[x]
            if nums[x] in dic:
                return [dic[nums[x]],x]
            dic[a] = x

    def threeSum(self, nums):
        """
        不涉及索引的，可以用排序+双指针的方法
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        numsi = sorted(nums)

        for i in range(n):
            if i >0 and numsi[i] == numsi[i-1]:
                continue
            index2 = n-1
            for index1 in range(i+1,n):
                if index1 > i+1 and numsi[index1]== numsi[index1-1]:
                    continue
                while index1 < index2 and numsi[index1] + numsi[index2] > 0 - numsi[i]:
                    index2 -=1
                if index1 == index2:
                    break
                if numsi[index1] + numsi[index2] == 0 - numsi[i]:
                    res.append([numsi[i], numsi[index1], numsi[index2]])
        return res

    def threeSum2(self, nums):
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def subarraySum(self, nums,k):
        """
        这个思路是比较套路的，有个前置条件举例来说：前缀和
        a3+a4 = (a0+a1+a2+a3+a4) - (a0+a1+a2) = pre(4) - pre(2) = pre(j) - pre(i-1)
        要连续子数组和为k 及 k = pre[j] - pre(i-1)  pre(i-1) = pre(j)-k
        需要一个辅助 dic 来存acc
        :param nums: 
        :return: 
        """
        dic = {}
        acc = 0
        count = 0
        for x in nums:
            acc += x
            if acc == k:
                count +=1
            if acc - k in dic:
                count += dic[acc - k]
            if acc in dic:
                dic[acc] +=1
            else:
                dic[acc] = 1
        return count

    def checkSubarraySum(self, nums, k):
        """
        给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，
        其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，其中 n 也是一个整数。
        这道题同样沿用了前缀和，但其中有一个关键点(count - count%k) % k == 0

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {0:-1}
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if k == 0:
                tmp = count
            else:
                tmp = count % k
            if tmp in hashmap:
                if i - hashmap[tmp] > 1:
                    return True
            else:
                hashmap[tmp] = i
        return False

    def findMedianSortedArrays(self, nums1,nums2):
        def getKthElement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2.

    def removeDuplicates(self, nums):
        """
        删除排序数组中的重复项
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <2:
            return len(nums)
        cur = 1
        while (cur < len(nums)):
            if nums[cur-1] == nums[cur]:
                nums.pop(cur)
            else:
                cur+=1
        return len(nums)

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        count = 1
        cur = 1
        while(cur< len(nums)):
            if nums[cur-1] == nums[cur]:
                count+=1

                if count > 2:
                    nums.pop(cur)
                    cur -=1
            else:
                count = 1
            cur+=1


        for item in nums:
            print item
        return len(nums)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) < 1:
            return
        cur = 0
        while (cur < len(nums)):
            if val == nums[cur]:
                nums.pop(cur)
            else:
                cur += 1
        for item in nums:
            print item
        return len(nums)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s
        substr = ""
        maxstr = ""
        maxlen = 0
        for i in range(n):
            if n - i <= maxlen:
                return maxstr
            for j in range(i + maxlen, n + 1):
                substr = s[i:j]
                if substr == substr[::-1]:
                    maxstr = substr
                    maxlen = j - i

        return maxstr


    def longestPalindrome2(self, s):

        if not s or len(s) <= 0:
            return ''

        maxLen = 0
        maxLenStr = ''

        strLen = len(s)
        for leftIdx in range(strLen):
            if strLen - leftIdx <= maxLen:
                return maxLenStr
            for rightIdx in range(leftIdx + maxLen, strLen + 1):
                subStr = s[leftIdx:rightIdx]
                # print(subStr)
                if subStr == subStr[::-1]:
                    maxLen = rightIdx - leftIdx
                    maxLenStr = subStr
        return maxLenStr

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ans = ""
        strtras = zip(*strs)
        for i in strtras:
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


print Solution().longestCommonPrefix(["aca","cba"])







