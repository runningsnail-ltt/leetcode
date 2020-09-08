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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
        return max(left_height,right_height)+1
    def Depth(self,root):
        if root is None:
            return -1
        else:
            return max(self.Depth(root.left),self.Depth(root.right))+1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if abs(self.Depth(root.left)-self.Depth(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val]+inorder(r.right) if r else []
        return inorder(root)[k-1]

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(root,val):
            if not root:
                return -1
            if root.val > val:
                return root.val
            left = preorder(root.left,val)
            right = preorder(root.right,val)
            if left<0:return right
            if right<0:return left
            return min(left,right)
        return preorder(root,root.val)
    def __init__(self):
        self.maxsum = float("-inf")

    def maxPathSum(self,root):
        def maxGain(root):
            if not root:
                return 0
            leftGain = max(0,maxGain(root.left))
            rightGain = max(0,maxGain(root.right))

            sumGain = root.val + leftGain+rightGain

            self.maxsum=max(self.maxsum,sumGain)

            return root.val + max(leftGain,rightGain)
        maxGain(root)
        return self.maxsum

    def constructMaximumBinaryTree(self, nums):
        """
        key1：最大值为root
        key2:左右部分分别找最大点作为子树的root，继续向下切分
        key3:递归
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        maxnode = max(nums)
        index = nums.index(maxnode)
        tree = TreeNode(maxnode)
        tree.left = self.constructMaximumBinaryTree(nums[:index])
        tree.right = self.constructMaximumBinaryTree(nums[index+1:])
        return tree

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

    def recoverFromPreorder(self, nums):
        """
        输入："1-2--3--4-5--6--7" 加的- 是为了更好的区分左右子树
        先验 前序：根左右
        二叉搜索树：根节点> 左子树所有节点 & 根节点< 右子树所有节点 
        :param nums: 
        :return: rtype: TreeNode
        """
        path, pos = list(), 0
        while pos < len(nums):
            level = 0
            while nums[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(nums) and nums[pos].isdigit():
                value = value * 10 + (ord(nums[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]




