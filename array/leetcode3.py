#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ls = list(s)
        n = len(s)
        if (n < 1):
            return 0
        # 维护一个滑动窗口ls[i...j]字串
        i = 0
        j = 0
        l = 1

        while i <= n-1:
            #python切片a[i,j+1]并不包括j+1
            if j+1 < n and s[j+1] not in s[i : j+1]:
                j += 1
                
            else:
                i += 1
            
            if j - i + 1 > 0:
                l = max(l, j - i + 1)

        return l

obj = Solution()
print(obj.lengthOfLongestSubstring('abcabcbb'))