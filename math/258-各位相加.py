class Solution:
    '''各位相加，直到结果是一位数为止'''

    def addDigits(self, num: int) -> int:
        str_num = str(num)
        if len(str_num)<2:
            return int(str_num)
        while len(str_num)>1:
            res = 0
            for i in range(len(str_num)):
                res += int(str_num[i])
            if res < 10:
                return res
            else:
                str_num = str(res)


if __name__ == '__main__':
    s  = Solution()
    print(s.addDigits(38))
