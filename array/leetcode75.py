#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''

class Solution:
    def sortColors(self, nums):
        n = len(nums)

        lt = -1
        gt = n
        i = 0

        while i < gt:
            if nums[i] == 0:
                lt += 1
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
            elif nums[i] == 2:
                gt -= 1
                nums[gt], nums[i] = nums[i], nums[gt]
            else:
                i += 1
        return nums

solution = Solution()
a = [2,0,2,1,1,0]
solution.sortColors(a)
print(a)