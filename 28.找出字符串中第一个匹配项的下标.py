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
        next = [0] * (len(needle) + 1)
        res = []
        j, i = 2, 0
        while j <= len(needle):
            while i > 0 and needle[j - 1] != needle[i]:
                i = next[i]
            if needle[j - 1] == needle[i]:
                i += 1
            next[j] = i
            j += 1
        i, j = 0, 0
        while i < len(haystack):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                res.append(i - j + 1)
                j = next[j]
            i += 1
        if len(res) > 0:
            return res[0]
        return -1

# @lc code=end

# @History 2021/7/6 start
class HistorySolution:
    def strStr1(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
# @History 2021/7/6 end