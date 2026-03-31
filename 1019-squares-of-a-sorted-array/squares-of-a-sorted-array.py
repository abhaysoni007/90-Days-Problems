class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newarr=[]
        for i in range(len(nums)):
            x=nums[i]**2
            newarr.append(x)
        newarr.sort()
        return newarr
