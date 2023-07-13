class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #make 2 passes, one in order, one in reverse, to complete products
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
            