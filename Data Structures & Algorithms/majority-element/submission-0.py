class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if(nums[i] not in count):
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        values = list(count.values())
        value = values.index(max(values))
        key = list(count.keys())
        return key[value]