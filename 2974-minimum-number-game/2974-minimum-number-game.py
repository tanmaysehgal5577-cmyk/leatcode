class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        
        # Swap adjacent elements pairwise
        for i in range(0, len(nums), 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
            
        return nums