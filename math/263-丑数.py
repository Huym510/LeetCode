class Solution:
    def isUgly(self, num):
        while num > 0 and num % 2 == 0:
            num = num / 2
        while num > 0 and num % 3 == 0:
            num = num / 3
        while num > 0 and num % 5 == 0:
            num = num / 5
        return True if num == 1.0 else False


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(25))