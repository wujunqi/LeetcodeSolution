#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        n = len(s)
        i = 0
        j = n-1

        while i < j:
            if s[i].isalnum() == False:
                i += 1
                continue
            if s[j].isalnum() == False:
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

obj = Solution()
print(obj.isPalindrome("race a car"))
