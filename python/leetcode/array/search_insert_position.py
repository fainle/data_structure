from typing import List


class Solution:
    """
    搜索索引位置
    id: 35
    时间复杂度: O(n)
    空间复杂度: O(1)
    """

    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if target <= v:
                return i
        return len(nums)


solution = Solution()

assert solution.search_insert(nums=[1, 3, 5, 6], target=5) == 2
assert solution.search_insert(nums=[1, 3, 5, 6], target=2) == 1
assert solution.search_insert(nums=[1, 3, 5, 6], target=7) == 4
assert solution.search_insert(nums=[1, 3, 5, 6], target=0) == 0
