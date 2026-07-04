class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # num1Index = { n: i for i , n in enumerate(nums1) }
        # res = [-1] * len(nums1)

        # stack = []
        # for i in range(len(nums2)):
        #     cur = nums2[i]
        #     while stack and cur > stack[-1]:
        #         val = stack.pop()
        #         idx = num1Index[val]
        #         res[idx] = cur
        #     if cur in num1Index:
        #         stack.append(cur)
        # return res

        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1

        result = []

        for num in nums1:
            result.append(next_greater[num])

        return result
