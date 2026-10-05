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
        for groupWords in seen.values():
            result.append(groupWords)
        return result