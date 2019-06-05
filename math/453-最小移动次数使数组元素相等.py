class Solution:
    '''给定一个长度为 n 的非空整数数组，
    找到让数组所有元素相等的最小移动次数。
    每次移动可以使 n - 1 个元素增加 1。

    思路：数组里每个值与最小值差值的和为最小次数
    '''
    # 自己的解法
    def minMoves(self, nums):
        # 1.找到最小值
        min = nums[0]
        for i in range(len(nums)):
            if min > nums[i]:
                min = nums[i]

        # 2.做差求和
        sum = 0
        for i in range(len(nums)):
            diff = nums[i] - min
            sum += diff
        return sum


    # 别人的解法
    def minMoves2(self, nums):
        sum = 0
        minmum = min(nums)
        for i in nums:
            sum += i - minmum
        return sum

