# -*- coding:utf-8 -*-
import os
import sys
from collections import Counter


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            # 计算当前节点下一个节点
            temp = cur.next
            # 将当前节点指向指向pre
            cur.next = pre
            # pre 和cur 都前进一步
            pre = cur
            cur = temp
        return pre

    def reverseBetween(self, head,m,n):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        flag_p = dummy  # 标志指针，帮助我们来找到要开始反转的那个节点的上一个节点
        pos = 0  # 位置，记录当前走到哪个位置
        while flag_p:
            # 判断当前的位置是不是位置 m 的上一个位置
            # 是的话
            if pos == m - 1:
                interrupts_node = flag_p  # 最终 interrupts_node 节点的 next 节点是反转区间的最后一个
                reverse_node = flag_p.next  # 要反转的开始节点
                sub_cur = None  # 子
                first_reverse_node = flag_p.next  # 第一个反转点的指针 first_reverse_node，这个指针最终要指向最后一个反转指针的下一个指针
                while pos < n:  # 如果当前位置在 小于位置 n，那么说明需要反转该节点
                    # 下面就是常规的链表反转
                    node = reverse_node.next  #
                    reverse_node.next = sub_cur
                    sub_cur = reverse_node
                    reverse_node = node
                    pos += 1
                # 两个关键的指针需要指向正确的位置
                interrupts_node.next = sub_cur
                first_reverse_node.next = node
                break

            # 不是的话往下走
            flag_p = flag_p.next
            pos += 1
        return dummy.next

    def addTwoNumbersReverse(self, l1,l2):
        start0 = ListNode(0)
        node = start0
        carry = 0
        s =0
        while(l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + carry
            carry = s / 10
            val = s % 10
            node.next = ListNode(val)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            node = node.next

        if carry!=0:
            node.next = ListNode(1)
        return start0.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        s1 = 0
        s2 = 0
        while l1:
            s1 = s1 *10 + l1.val
            l1 = l1.next
        while l2:
            s2 = s2*10 + l2.val
            l2 = l2.next
        s3 = s1+s2
        start = ListNode(0)
        node = start
        for x in (str(s3)):
            node.next = ListNode(x)
            node = node.next
        return start.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        node = start
        while (l1 and l2):
            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next
        while (l1):
            node.next = ListNode(l1.val)
            l1 = l1.next
            node = node.next
        while (l2):
            node.next = ListNode(l2.val)
            l2 = l2.next
            node = node.next
        return start.next

    def mergeKLists(self, lists):
        """
        先遍历链表得到每个节点的值 2.对节点值进行排序 3.再依次放入新的链表中
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        arr = []
        for item in lists:
            while(item):
                arr.append(item.val)
                item = item.next
        arr.sort()
        start = ListNode(0)

        node = start
        for item in arr:
            node.next = ListNode(item)
            node = node.next
        return start.next

    def sortList(self, head):
        """
        先遍历链表得到每个节点的值 2.对节点值进行排序 3.再依次放入新的链表中
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        start = ListNode(0)
        node = start
        while(head):
            arr.append(head.val)
            head = head.next
        arr.sort()

        for item in arr:
            node.next = ListNode(item)
            node = node.next
        return start.next

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = ListNode(0)
        cur = head
        n = 0
        low = p
        fast = p
        p.next = head
        while cur:

            cur = cur.next
            n = n+ 1
        if n == 0 or k % n == 0:
            return head
        n = k % n
        while fast.next and n >0:
            fast = fast.next
            n = n-1

        while fast.next:
            low = low.next
            fast = fast.next
        fast.next = head
        p.next = low.next
        low.next = None
        return p.next

    def hasCycle(self, head):
        """
        使用快慢指针，一开始傻逼了
        :param head: 
        :return: 
        """
        fast = head
        low = head
        while(low and fast.next):
            low = low.next
            fast = fast.next.next
            if not fast:
                return False
            if fast == low:
                return True
        return False




    def getCycle(self, head):
        fast = head
        low = head
        while (low and fast.next):
            low = low.next
            fast = fast.next.next
            if not fast:
                return None
            if low == fast:
                return low
        return None

    def detectCycle(self, head):
        """
        Floyd 算法：双指针
        第一阶段：判断链表是否有环；
        第二阶段：首先我们初始化额外的两个指针： ptr1 ，指向链表的头， ptr2 指向相遇点。然后，我们每次将它们往前移动一步，直到它们相遇，它们相遇的点就是环的入口，返回这个节点
    
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None
        intersect = self.getCycle(head)
        if intersect is None:
            return None
        prt = head
        meet = intersect
        while (prt != meet):
            prt = prt.next
            meet = meet.next
        return prt

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        len1 = 0
        len2 = 0
        p = headA
        while (p):
            len1 += 1
            p = p.next
        p = headB
        while (p):
            len2 += 1
            p = p.next

        while (len1 > len2):
            headA = headA.next
            len1 -= 1
        while (len2 > len1):
            headB = headB.next
            len2 -= 1
        while (headA is not headB):
            headA = headA.next
            headB = headB.next
        return headA

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {x: list1.index(x)+list2.index(x) for x in list1 and list2}
        return [x for x in d if d[x] == min(d.values())]

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    # class ListNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.next = None

    class Solution:
        def sortList(self, head):
            """
            思路：其实就是类似于快排，找一个点，找到比他大的比他小的，然后最后合并起来即为有序的
            :param head: 
            :return: 
            """
            if head is None:
                return head

            # 分成三个链表
            large = None
            small = None
            equal = None
            cur = head

            while cur is not None:
                t = cur
                cur = cur.next
                if t.val < head.val:
                    t.next = small
                    small = t
                elif t.val > head.val:
                    t.next = large
                    large = t
                else:
                    t.next = equal
                    equal = t

            # 各自排序即可
            large = self.sortList(large)
            small = self.sortList(small)

            ret = ListNode(None)
            cur = ret

            # 将三个链表merge到一起
            for p in [small, equal, large]:
                while p is not None:
                    cur.next = p
                    p = p.next
                    cur = cur.next
                    cur.next = None
            return ret.next




def trans_pid(pid):
    return pid | 1 << 48
print trans_pid(87961109652684)











        








