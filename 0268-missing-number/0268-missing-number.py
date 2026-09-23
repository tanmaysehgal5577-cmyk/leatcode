class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Gauss's formula to find the sum of first n numbers
        expected_sum = n * (n + 1) // 2
        
        # The difference is exactly the missing number
        return expected_sum - sum(nums)