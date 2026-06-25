class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_1 = strs[0]
        for i in range(1,len(strs)):
            if(len(strs[i]) < len(str_1)):
                str_1 = strs[i]
        string = ""
        for i in range(len(str_1)):
            for j in range(len(strs)):
                if(strs[j][i] != str_1[i]):
                    return string
            string += str_1[i]
        return string
        
                
