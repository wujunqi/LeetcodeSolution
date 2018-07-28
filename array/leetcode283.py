#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: leetcode(283). 移动零
'''

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = -1
        j = 0
        # nums[0....i]表示非0元素的数列,初始值i=-1
        while j <= n-1:
            if nums[j] != 0:
                i += 1
                nums[i] = nums[j]
            j += 1
        for k in range(i+1, n):
            nums[k] = 0
        

solution = Solution()
a = [0,1,0,3,12]
solution.moveZeroes(a)
print(a)