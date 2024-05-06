# @before-stub-for-debug-begin
from python3problem28 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # l_n = len(needle)
        # l_s = len(haystack)
        # for i in range(l_s - l_n + 1):
        #     index = i
        #     j = i
        #     k = 0
        #     while j < l_s and k < l_n and haystack[j] == needle[k] :
        #         j += 1
        #         k += 1
        #     if k == l_n:
        #         return index
        
        # return -1

# @lc code=end

# @History 2021/7/6 start
class HistorySolution:
    def strStr1(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
# @History 2021/7/6 end