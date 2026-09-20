class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ''
        for s1, s2 in zip(strs[0], strs[-1]):
            if not strs:
                return False
            if s1 == s2:
                result += s1
            else:
                break
        return result