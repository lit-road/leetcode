# @before-stub-for-debug-begin
from python3problem21 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 208/208 cases passed (32 ms)
    # Your runtime beats 90.62 % of python3 submissions
    # Your memory usage beats 46.75 % of python3 submissions (16.4 MB)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_node = ListNode()
        list_node_header = list_node
        while list1 and list2:
            if list1.val < list2.val:
                list_node.next = list1
                list1 = list1.next
            else:
                list_node.next = list2
                list2 = list2.next
            list_node = list_node.next

        list_node.next = list1 if list1 else list2

        return list_node_header.next
# @lc code=end

# @History 2021/7/6 start

class HistorySolution:
    # 208/208 cases passed (30 ms)
    # Your runtime beats 95.52 % of python3 submissions
    # Your memory usage beats 48.4 % of python3 submissions (16.4 MB)
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_node = ListNode()
        list_node_header = list_node
        while list1 and list2:
            if list1.val < list2.val:
                list_node.next = list1
                list1 = list1.next
            else:
                list_node.next = list2
                list2 = list2.next
            list_node = list_node.next

        while list1:
            list_node.next = list1
            list1 = list1.next
            list_node = list_node.next
        while list2:
            list_node.next = list2
            list2 = list2.next
            list_node = list_node.next

        return list_node_header.next
    
    # 208/208 cases passed (43 ms)
    # Your runtime beats 27.66 % of python3 submissions
    # Your memory usage beats 89.04 % of python3 submissions (16.3 MB)
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_node = ListNode()
        list_node_header = list_node
        while list1 and list2:
            if list1.val < list2.val:
                list_node.next = list1
                list1 = list1.next
            else:
                list_node.next = list2
                list2 = list2.next
            list_node = list_node.next

        if list1:
            list_node.next = list1
        if list2:
            list_node.next = list2

        return list_node_header.next
    
# @History 2021/7/6 end