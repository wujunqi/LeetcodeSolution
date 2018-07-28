#coding=utf-8
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0 or n==1:
            return n

        # nums[0,i]为非重复数列
        i = 0
        j = i + 1
        while j <= n-1:
            if nums[j] != nums[i]:
                # 指向同一个元素不需要赋值
                if i + 1 != j:
                    nums[i+1] = nums[j]
                i += 1
            j += 1
        return i + 1

solution = Solution()
a = [0,0,1,1,1,2,2,3,3,4,5,5,8,8,8,9]
print(solution.removeDuplicates(a))
print(a)