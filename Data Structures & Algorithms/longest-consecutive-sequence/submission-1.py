class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        numset = set(nums)

        for n in nums:
            if n - 1 not in numset:
                length = 1
                while n + length in numset:
                    length += 1
                output = max(output, length)
        return output

            