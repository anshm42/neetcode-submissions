class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        answer = []

        for i in range(len(nums)):
            if target - nums[i] in hs:
                answer.append(hs[target - nums[i]])
                answer.append(i)
            else: 
                hs[nums[i]] = i
        return answer
        