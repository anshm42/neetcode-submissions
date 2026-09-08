class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = math.floor((l + r)/2)
            if nums[m] == target:
                return m
            elif nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            elif nums[m] <= nums[r]:
                if target > nums[m] and target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] >= nums[l]:
                if target < nums[m] and target > nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1   
            
