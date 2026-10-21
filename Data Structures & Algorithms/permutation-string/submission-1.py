class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        need = {}
        for ch in s1:
            need[ch] = need.get(ch,0)+1
        
        window = {}
        for right,ch in enumerate(s2):
            window[ch] = window.get(ch,0)+1
            if right >= n:
                left_ch = s2[right - n]
                window[left_ch] -= 1
                if window[left_ch] == 0:
                    del window[left_ch]
            if window == need:
                return True
        return False

        