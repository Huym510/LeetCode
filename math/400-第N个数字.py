class Solution:
    '''
    首先阐明题意：
    在1 2 3 4 5 6 7 8 9 10 11 12....找第n个数
    把这些自然数看做是列表，找到下标为n-1（列表从0开始计数）的那个数
    意味着10被拆成1和0，10 变成了两个数，同理12拆成1和2，变成两个数...
    所以当n=11时，就是10中的那个0

    这些数字有如下规律
    1位数：1-9 9*10**(1-1)*1=9 共有9个数
    2位数：10-99 9*10**(2-1)*2=180 共有180个数
    3位数：100-999 9*10**(3-1)*3=2700 共有2700个数
    4位数：1000-9999 9*10**(4-1)*4=36000 共有2700个数
    ......
    n位数： 9*10**(n-1)*n
    '''

    def findNthDigit(self, n: int):
        # 1.先找出这个数是几位数digit
        digit = 1
        while n > 9 * 10 ** (digit - 1) * digit:
            n -= 9 * 10 ** (digit - 1) * digit
            digit += 1
        # 当结束循环后，此时的digit就是n的位数 n变成了digit位数的起始值

        # 2.确定是digit范围内的那个第a个数
        a = int((n - 1) / digit)  # (n-1)是因为
        # 3.确定是digit范围内数a的第几个位置
        b = (n - 1) % digit
        num = 10 ** (digit - 1) + a  # 定位到num
        res = list(str(num))[b:b + 1]  # 切割num,得到num上的第b位数，即为所求
        return int(''.join(res))  # 将列表res转换成数字


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(11))
