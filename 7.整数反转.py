#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1
        x = int(str(x)[::-1]) * flag
        if x < -2**31 or x > 2**31 -1:
            return 0
        return x
# @lc code=end

# @history start
class HistorySolution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1
        x = int(str(x)[::-1]) * flag
        if x < -2**31 or x > 2**31 -1:
            return 0
        return x
# @history end

