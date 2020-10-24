from typing import List


class Solution:
    """
    寻找中心索引
    id: 724
    时间复杂度: O(n)
    空间复杂度: O(1)
    """

    @staticmethod
    def pivot_index(nums: List[int]) -> int:
        S = sum(nums)

        left_sum = 0

        for i, x in enumerate(nums):
            if left_sum == (S - left_sum - x):
                return i

            left_sum += x
        return -1


solution = Solution()

assert solution.pivot_index(nums=[1, 2]) == -1
assert solution.pivot_index(nums=[1, 7, 3, 6, 5, 6]) == 3
assert solution.pivot_index(nums=[1, 2, 3]) == -1
assert solution.pivot_index(nums=[-1, -1, -1, -1, -1, 0]) == 2
