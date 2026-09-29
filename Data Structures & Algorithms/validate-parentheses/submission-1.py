class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(',']':'[','}':'{'}
        for bracket in s:
            if stack and bracket in hashmap and stack[-1] == hashmap[bracket]:
                stack.pop()
            else:
                stack.append(bracket)
        return not stack