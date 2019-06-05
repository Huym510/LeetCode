class Solution:
    def isPowerofThree(self, n):
        while n > 0 and n % 3 == 0:
            n = n / 3
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerofThree(9))
