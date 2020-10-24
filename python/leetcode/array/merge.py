from typing import List


class Solution:
    """
    合并区间数组
    id: 56
    时间复杂度 O(n logn)
    空间复杂度: O(logn)
    """

    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:

        # 注意先排序
        intervals.sort(key=lambda x: x[0])

        res = []
        if len(intervals) <= 0:
            return []

        tmp = intervals[0]
        for i in intervals[1:]:
            if tmp[1] >= i[0]:
                tmp[1] = max(tmp[1], i[1])
            else:
                res.append(tmp)
                tmp = i

        res.append(tmp)
        return res


solution = Solution()

assert solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert solution.merge(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
assert solution.merge(intervals=[[1, 4], [0, 1]]) == [[0, 4]]
