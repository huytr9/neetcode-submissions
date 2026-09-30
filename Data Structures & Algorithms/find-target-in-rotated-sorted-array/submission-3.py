class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                # Target is inside the left side
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # Target must be on the right side
                else:
                    l = m + 1
            # Right side is sorted
            else:
                # Target is inside the right side
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # Target must be on the left side
                else:
                    r = m - 1
        return -1