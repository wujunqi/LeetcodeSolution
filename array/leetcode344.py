#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        i = 0
        j = n - 1
        a = ''
        while(j >= 0):
            a += s[j]
            j -= 1
        return a