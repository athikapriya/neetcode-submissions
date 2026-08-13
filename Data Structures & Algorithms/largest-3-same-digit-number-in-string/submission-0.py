class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""

        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if largest == "" or num[i] > largest[0]:
                    largest = num[i] * 3
                
        return largest