class Solution:
    def arrangeCoins(self, n: int):
        i = 0
        sum = 0
        if n == 0:
            return n
        while True:
            sum += i
            if n - sum < i+1:
                return i
            i += 1


if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(1))
