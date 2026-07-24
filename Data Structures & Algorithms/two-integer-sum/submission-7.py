class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, n in enumerate(nums):
            found[n] = i
        for i, n in enumerate(nums):
            complement = target - n
            if complement in found and found[complement] != i:
                return [i, found[complement]]
        return []
        