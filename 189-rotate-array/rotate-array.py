class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        new = []
        k = k % len(nums)

        for i in range(len(nums) - k, len(nums)):
            new.append(nums[i])

        for i in range(0, len(nums) - k):
            new.append(nums[i])

        for i in range(len(nums)):
            nums[i] = new[i]