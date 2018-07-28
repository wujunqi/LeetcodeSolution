#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        s_len, p_len = len(s), len(p)
        count = p_len
        pChar = Counter(p)

        result = []
        for i in range(s_len):
            if pChar[s[i]] >= 1:
                count -= 1
            pChar[s[i]] -= 1
            if i >= p_len:
                if pChar[s[i - p_len]] >= 0:
                    count += 1
                pChar[s[i - p_len]] += 1
            if count == 0:
                result.append(i - p_len + 1)

        return result

obj = Solution()
print(obj.findAnagrams("ababababab", "aab"))