#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0
        j = n - 1

        sum = (j - i) * min(height[i], height[j])
        
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            sum = max(sum, (j - i) * min(height[i], height[j]))
            
        return sum