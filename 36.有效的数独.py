#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 同行不重复
        # 同列不重复
        # 同3x3宫格不重复
        for i in range(9): # 行
            for j in range(9): # 列
                if board[i][j] == '.':
                    continue
                # 判断是否重复
                for k in range(9):
                    if board[i][j] == board[i][k] or board[i][j] == board[k][j]:
                        return False
                    elif 

# @lc code=end

