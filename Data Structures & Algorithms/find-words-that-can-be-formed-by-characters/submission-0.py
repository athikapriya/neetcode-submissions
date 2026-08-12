class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = {}
        count = 0

        for char in chars:
            freq[char] = freq.get(char, 0) + 1

        for word in words:
            word_freq = {}
            
            for char in word:
                word_freq[char] = word_freq.get(char, 0) + 1

            can_form = True

            for char in word_freq:
                if word_freq[char] > freq.get(char, 0):
                    can_form = False
                    break
                
            if can_form:
                count += len(word)
            
        return count
