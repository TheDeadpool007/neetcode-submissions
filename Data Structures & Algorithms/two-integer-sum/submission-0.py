class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} # val : index

        for i, curr in enumerate (nums):
            diff = target - curr
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[curr] = i
        return


    