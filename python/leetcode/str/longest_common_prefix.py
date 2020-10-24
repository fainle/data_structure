from typing import List


class Solution:
    """
    最长公共前缀
    id: 14
    时间复杂度:
    空间复杂度:
    """

    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        min_len = min([len(s) for s in strs])
        lc = ""

        for i in range(min_len):
            p = [s[i] for s in strs]
            if len(set(p)) != 1:
                break
            else:
                lc += p[0]
        return lc


solution = Solution()

assert solution.longest_common_prefix(strs=["flower", "flow", "flight"]) == 'fl'
assert solution.longest_common_prefix(strs=["dog", "racecar", "car"]) == ''
