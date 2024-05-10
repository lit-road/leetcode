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
                    if j != k and board[i][j] == board[i][k] or i != k and board[i][j] == board[k][j]:
                        return False
                # 判断3x3宫格
                i_begin, j_begin = i // 3 * 3, j // 3 * 3
                for m in range(i_begin, i_begin + 3):
                    for n in range(j_begin, j_begin + 3):
                        if i != m and j != n and board[i][j] == board[m][n]:
                            return False

        return True

# @lc code=end

# @history 2021/7/6 start
class HistorySolution:
    # 507/507 cases passed (56 ms)
    # Your runtime beats 7.92 % of python3 submissions
    # Your memory usage beats 41.93 % of python3 submissions (16.4 MB)
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        # 同行不重复
        # 同列不重复
        # 同3x3宫格不重复
        for i in range(9): # 行
            for j in range(9): # 列
                if board[i][j] == '.':
                    continue
                # 判断是否重复
                for k in range(9):
                    if j != k and board[i][j] == board[i][k] or i != k and board[i][j] == board[k][j]:
                        return False
                # 判断3x3宫格
                i_begin, j_begin = i // 3 * 3, j // 3 * 3
                for m in range(i_begin, i_begin + 3):
                    for n in range(j_begin, j_begin + 3):
                        if i != m and j != n and board[i][j] == board[m][n]:
                            return False

        return True
# @history 2021/7/6 end

# @test start
def test_valid_sudoku_board(self):
    solution = HistorySolution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku1(board) == True

def test_one_cell_filled(self):
    solution = HistorySolution()
    board = [
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".","5",".",".",".","."],
        [".",".",".",".",".","5",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
    ]
    assert solution.isValidSudoku1(board) == False
# @test end