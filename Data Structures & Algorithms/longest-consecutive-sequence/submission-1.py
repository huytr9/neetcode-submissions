class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:

            # Only start counting if num is the beginning
            # of a consecutive sequence
            if num - 1 not in seen:

                current = num
                length = 1

                # Count forward:
                # num, num+1, num+2, ...
                while current + 1 in seen:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest