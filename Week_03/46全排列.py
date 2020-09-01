
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

#tmp_res,初始值为[]
        def backtrack(nums, tmp_res):

###终止条件，nums中元素遍历完了
            if not nums:
                res.append(tmp_res)
                return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp_res + [nums[i]])

        backtrack(nums, [])
        return res