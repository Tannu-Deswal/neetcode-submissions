class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen1 = {}
        for str1 in s:
            if str1 in seen:
                seen[str1]+=1
            else:
                seen[str1] = 1
        for str2 in t:
            if str2 in seen1:
                seen1[str2]+=1
            else:
                seen1[str2] = 1
        return seen == seen1