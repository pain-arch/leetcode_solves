class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                diff_i = hashmap[nums[i]]
                return [diff_i, i]
            else :
                diff = target - nums[i]
                hashmap[diff] = i    