def sums(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum(nums[1:])


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    assert sums(nums) == 10
