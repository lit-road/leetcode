# @before-stub-for-debug-begin
from python3problem42 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_size = 0
        while left < right:
            # 更新左右最大值
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max < right_max:
                water_size += left_max - height[left]
                left += 1
            else:
                water_size += right_max - height[right]
                right -= 1
        return water_size


# @lc code=end

# @history 2024/05/01 start
class nodeInfo:
    def __init__(self) -> None:
        self.MaxLeft = 0
        self.MaxRight = 0
        # self.Height = 0

class HistorySolution:
    # 这个方法没考虑 4,2,3的情况
    def trap1(self, height: List[int]) -> int:
        # 两边肯定没有积水
        # 从第一个开始，向右计算积水
        # 记录当前元素，最靠近的等高或者是更高的元素，获得其位置
        # 累加积水
        water = 0
        def get_first_right_max_water(height, index):
            for i in range(index+1, len(height)):
                if i < len(height) and height[i] >= height[index]:
                    return i - 1
            return 0
        for i in range(len(height)):
            if i == 0:
                continue
            right = get_first_right_max_water(height, i)
            water += right
        return water
    
    # 322/322 cases passed (73 ms)
    # Your runtime beats 8.2 % of python3 submissions
    # Your memory usage beats 5.03 % of python3 submissions (19.4 MB)
    # 耗时 20:15:25
    def trap2(self, height: List[int]) -> int:
        # 计算每个位置上面的水量
        # 每个位置上面的水受到左右的影响
        # 计算每个位置左右的高度
        nodeInfos = [nodeInfo() for i in range(len(height))]
        waterSize = 0
        for i in range(len(height)):
            # nodeInfos[i].Height = height[i]
            nodeInfos[i].MaxLeft = height[i] if i == 0 else max(nodeInfos[i-1].MaxLeft, height[i])
            # from right to left
            j = len(height) - i - 1
            nodeInfos[j].MaxRight = height[j] if i == 0 else max(nodeInfos[j+1].MaxRight, height[j])
        
        for i in range(len(height)):
            left = nodeInfos[i].MaxLeft
            right = nodeInfos[i].MaxRight
            currentHeight = height[i] # nodeInfos[i].Height
            if currentHeight < left and currentHeight < right:
                waterSize += min(left, right) - currentHeight
        return waterSize
    

    def trap3(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_size = 0
        while left < right:
            # 更新左右最大值
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max < right_max:
                water_size += left_max - height[left]
                left += 1
            else:
                water_size += right_max - height[right]
                right -= 1
        return water_size
    
# @history 2024/05/01 end