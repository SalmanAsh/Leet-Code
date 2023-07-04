class Solution:
    def palindromicSubstrings(self, s: str) -> int:
        resCount = 0
        
        for i in range(len(s)):
            # Odd Length
            l, r = i, i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                resCount += 1
                l -= 1
                r += 1
            
            # Even Length
            l, r = i, i + 1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                resCount += 1
                l -= 1
                r += 1
        
        return resCount
            