class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(t) != len(s)):
            return False
        string_1 = set()
        for i in s:
            string_1.add(i)

        for i in string_1:
            if(s.count(i) != t.count(i)):
                return False
        return True        