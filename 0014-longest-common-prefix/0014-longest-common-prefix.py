class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                # If index exceeds current string OR mismatch occurs
                if i >= len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
