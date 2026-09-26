class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashSet = set()
        left = 0
        longest = 0

        for right in range(len(s)):

            # If duplicate, move left forward
            # until the duplicate is removed
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1

            # Add current character
            hashSet.add(s[right])

            # Current window length
            longest = max(longest, right - left + 1)

        return longest