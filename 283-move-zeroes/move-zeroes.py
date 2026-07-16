class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # new=[]
        # while 0 in nums:
        #     new.append(0)
        #     nums.remove(0)
        # nums.extend(new)
        # return nums
        left=0
        right=left+1
        while right < len(nums):
            if nums[left] != 0:
                left += 1
                if left == right:
                    right += 1
            elif nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1

        return nums
























        # start=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[i],nums[start]=nums[start],nums[i]
        #         start+=1 

        