class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        answer = []

        for i in range(len(nums)):
            if target - nums[i] in m:
                answer.append(m[target - nums[i]])
                answer.append(i)
                return answer
            else:
                m[nums[i]] = i
        