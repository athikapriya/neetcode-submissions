class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        repeat = -1
        missing = -1

        for row in grid:
            for num in row:
                if num in seen:
                    repeat = num
                else:
                    seen.add(num)
        
        for num in range(1, len(grid) * len(grid) + 1):
            if num not in seen:
                missing = num
                break

        return [repeat, missing]