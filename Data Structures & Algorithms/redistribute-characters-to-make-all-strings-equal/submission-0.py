class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = [0] * 26

        for word in words:
            for ch in word:
                count[ord(ch) - ord('a')] += 1
        
        n = len(words)

        for freq in count:
            if freq % n != 0:
                return False
            
        return True