#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''

class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        if (n < 2):
            return []
        i = 0
        j = n-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i,j]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return []
