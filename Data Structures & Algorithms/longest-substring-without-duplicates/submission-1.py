class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        longest = 0 
        l = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            w = (r - l) + 1
            longest = max(longest, w)
            hashset.add(s[r])
        return longest