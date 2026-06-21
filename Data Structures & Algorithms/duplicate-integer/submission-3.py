class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original = set()             #using set for unique values because it hashes the values inside it
        for num in nums:             #making it easier to search 
            if num in original:
                return True
            original.add(num)
        return False
        
        
        