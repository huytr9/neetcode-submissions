class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]
        result = []
        for group in seen.values():
            result.append(group)
        return result