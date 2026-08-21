class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        ans = 0

        for freq in count.values():
            ans += freq - (freq % 2)

        if ans < len(s):
            ans += 1
        
        return ans