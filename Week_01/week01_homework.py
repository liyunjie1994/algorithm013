#
# arr=input("")
# num = [int(n) for n in arr.split(' ')]
#１
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         for i in range(len(nums)-1,0,-1):
#             if nums[i] == nums[i-1]:
#                 nums.pop(nums[i])
#         return len(nums)
#         return nums

######
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         lenth = len(nums)
#         nums[:] = nums[lenth-k:] + nums[:lenth-k]

####合并两个有序链表
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1:return l2
#         if not l2:return l1
#         if l1.val <= l2.val:
#             l1.next = self.mergeTwoLists(l1.next,l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1,l2.next)
#             return l2


##两数之和
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         if len(nums) <= 1:return False
#         buff_dict = {}
#         for i in range(len(nums)):
#             if nums[i] in buff_dict:
#                 return[buff_dict[nums[i]],i]
#             else:
#                 buff_dict[target-nums[i]] = i

###移动零
# def moveZeroes(self, nums):
#     zero = 0  # records the position of "0"
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[zero] = nums[zero], nums[i]
#             zero += 1

##加一
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         value = 0
#         for i in range(len(digits)):
#             value = value + digits[i] * pow(10, (len(digits) - i - 1))
#         value = value + 1
#
#         return [int(i) for i in str(value)]