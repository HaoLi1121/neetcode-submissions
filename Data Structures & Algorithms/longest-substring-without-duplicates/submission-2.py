class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_screen = {}
        left = 0
        best = 0
        for right,ch in enumerate(s):
            if ch in last_screen and last_screen[ch]>= left:
                left = last_screen[ch] + 1
            last_screen[ch] = right
            best = max(best, right - left + 1)
        return best
        