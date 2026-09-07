class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        ans = []
        index = 0
        for i in nums:
            if target - i in m:
                ans.append(m[target-i])
                ans.append(index)
            else: 
                m[i] = index
                index += 1
        return ans