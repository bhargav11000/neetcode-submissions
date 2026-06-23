class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i,n in enumerate(nums):
            d = target-n
            if(d in store):
                return [store[d],i]
            store[n] = i
        return []