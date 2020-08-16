def twosum(self,nums,target):
    if len(nums) <= 1:return False

    buffer = {}
    for i in range(len(nums)):
        if nums[i] in buffer:
            return [buffer[nums[i]], i ]
        else:
            buffer[target- nums[i]] = i