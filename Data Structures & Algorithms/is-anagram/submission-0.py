class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            list_s = list()
            list_t = list()
            for x in range(len(s)):
                list_s.append(s[x])
                list_t.append(t[x])
            list_s.sort()
            list_t.sort()
            if list_s == list_t:
                return True
            else:
                return False
                