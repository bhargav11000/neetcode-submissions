class Solution:
    def length(self,nums: List[int]) -> int:
        i = 0
        try:
            while(nums[i] or nums[i] == 0):
                i += 1
        except:
            return i
                
    def sortArray(self, nums: List[int]) -> List[int]:
        low = 0
        high = self.length(nums) - 1
        self.main(nums,low,high)
        return nums
    
    def main(self, nums: List[int],low: int,high: int) -> List[int]:
        if(low<high):
            mid = self.sort(nums,low,high)
            bottom = self.main(nums,low,mid-1)
            top = self.main(nums,mid+1,high)
        return nums
        
    def sort(self,lnums: List[int],low: int,high: int) -> int:
        mid_index = (low+high)//2
        lnums[mid_index],lnums[high] = lnums[high],lnums[mid_index]
        pivot = lnums[high]
        i = low -1
        j = low
        while(j<high):
            if(lnums[j] < pivot):
                i += 1
                lnums[i],lnums[j] = lnums[j],lnums[i]
            j += 1
        i += 1
        lnums[i],lnums[high] = lnums[high],lnums[i]
        return i
