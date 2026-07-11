class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        freq = {}
        count = 0

        for word in arr:
            freq[word] = freq.get(word, 0) + 1
        
        for word in arr:
            if freq[word] == 1:
                count += 1
                if count == k:
                    return word
        
        return ""
