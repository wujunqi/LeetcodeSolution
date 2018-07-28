#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = -1
        # 定义nums[0...i]为非val的数列
        j = 0
        while j <= n-1:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1
        

solution = Solution()
a = [0,1,2,2,3,0,4,2]
val = 2
print(solution.removeElement(a, 2))