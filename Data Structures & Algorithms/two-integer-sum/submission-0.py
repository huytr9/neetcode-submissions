class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i in range(len(nums)):
            hashSet[nums[i]] = i
        for i in range(len(nums)):
            y = target - nums[i]
            if y in hashSet and hashSet[y] != i:
                return [i, hashSet[y]]