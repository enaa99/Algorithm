from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        strings = deque()

        maxLength = 0
        for char in s:
            if char not in strings:
                strings.append(char)
                maxLength = max(maxLength, len(strings))
            else:
                while char in strings:
                    strings.popleft()
                strings.append(char)

        return maxLength