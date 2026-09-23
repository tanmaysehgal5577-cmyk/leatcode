class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return -1
        
        # Sirf pehle 3 elements uthao, unhe sort karo, aur middle wala return kardo
        return sorted(nums[:3])[1]