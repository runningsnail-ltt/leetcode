# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dic = Counter(s)
        # for i in range(len(s)):
        #     if dic[s[i]]==1:
        #         return i
        # return -1
        s_list = list(set(s))
        print s_list
        s_list.sort(key=s.index)
        print s_list
        for i in s_list:
            count = s.count(i)
            if count == 1:
                return s.index(i)
        return -1

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        needlelen = len(needle)
        for i in range(len(haystack)-needlelen+1):
            if needle == haystack[i:i+needlelen]:
                return i
        return -1


if __name__ == "__main__":

    solution = Solution()
    haystack = "hello"
    needle = "ll"
    print solution.strStr(haystack,needle)