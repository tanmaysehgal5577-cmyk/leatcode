class Solution(object):
    def containsDuplicate(self, nums):
        harset=set()

        for n in nums:
            if n in harset:
                
                return True
            harset.add(n)
        return False
        