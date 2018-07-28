#coding=utf-8
'''
@author: wujunqi
@email: jun_qi_wu@163.com
@desc: 
'''
class Solution:
    def merge(self, nums1, m, nums2, n):
        
        # 尾插入法 
        if (n < 1):
            return
        if (m < 1):
            nums1[0:n] = nums2[0:n]
            return
        k = m + n - 1
        i = m - 1
        j = n - 1

        while k >= 0:
            if (nums1[i] > nums2[j] and i >= 0) or (j < 0 and i >= 0):
                nums1[k] = nums1[i]
                k -= 1
                i -= 1

            if (nums2[j] >= nums1[i] and j >= 0) or (i < 0 and j >=0):
                nums1[k] = nums2[j] 
                k -= 1
                j -= 1

solution = Solution()

nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m,nums2, n)
print(nums1)
        