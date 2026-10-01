class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            y = target - n
            if y in hashmap:
                return [hashmap[y], i]
            hashmap[n] = i
        return