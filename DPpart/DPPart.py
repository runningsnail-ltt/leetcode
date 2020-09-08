# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f_1 = 1
        f_2 = 2
        if n == 1:
            return f_1
        if n == 2:
            return f_2
        for i in range(3,n+1):
            f_n = f_1+f_2
            f_1=f_2
            f_2 = f_n
        return f_n

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs(self, n) :
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]



    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        cur,pre = 0,0
        for i in range(len(cost)):
            cur,pre = min(cur,pre)+cost[i],cur
        return min(cur,pre)

    def uniquePaths(self, m,n):
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print dp
        return dp[-1][-1]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}

        def dp(n):
            res = float("inf")
            if n in memo: return memo[n]
            # base
            if n < 0:
                return -1
            if n == 0:
                return 0
            for coin in coins:

                subpro = dp(n - coin)
                if subpro == -1:
                    continue
                res = min(res, subpro + 1)


            memo[n] = res if res!= float("inf") else -1
            return memo[n]

        return dp(amount)

    def coinChangeA(self,coins, amount):
    # 备忘录
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)






print Solution().coinChange([1,2,5],11)