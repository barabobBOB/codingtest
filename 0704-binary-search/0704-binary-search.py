class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        for i in range(len(nums)):
            if target == nums[i]:
                answer = i
        return answer