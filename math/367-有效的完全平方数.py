class Solution:
    def isPerfectSquare(self, num):
        return num ** 0.5 == int(num ** 0.5)


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(16))
