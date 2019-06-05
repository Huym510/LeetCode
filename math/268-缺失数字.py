class Solution:

    def missingNumber(self, nums) -> int:
        nums.sort()
        # print(nums)
        sum = 0
        res = 0
        for i in range(nums[-1] + 1):
            sum += i
        # print("sum:", sum)
        for i in range(len(nums)):
            res += nums[i]
        # print("result:", res)
        num = sum - res
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1,2,5]))
