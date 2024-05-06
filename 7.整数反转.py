# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:
            # python3 取余 与 除数（10）符号保持一致，所以是 -123 % 10 = -13 ... 7
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
            if rev < INT_MIN or rev > INT_MAX:
                return 0
        return rev
# @lc code=end

# @history start
class HistorySolution:
    # Time complexity model: O(1)
    # Space complexity model: O(1)
    def reverse1(self, x: int) -> int:
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1
        x = int(str(x)[::-1]) * flag
        if x < -2**31 or x > 2**31 -1:
            return 0
        return x
    
    # Time complexity model: O(log|x|)
    def reverse2(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:
            # python3 取余 与 除数（10）符号保持一致，所以是 -123 % 10 = -13 ... 7
            digit = x % 10
            if x < 0 and digit > 0:
                digit -= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
            if rev < INT_MIN or rev > INT_MAX:
                return 0
        return rev
# @history end

