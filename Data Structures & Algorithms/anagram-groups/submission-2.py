class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        cat = {}
        pos = 0
        for i,n in enumerate(strs):
            temp_set = tuple(sorted(tuple(n)))
            if(temp_set in cat and len(strs[i]) == len(strs[cat[temp_set][1]])):
                groups[cat[temp_set][0]].append(strs[i])
            else:
                cat[temp_set] = (pos,i)
                groups.append([n])
                pos += 1
        return groups

            

        