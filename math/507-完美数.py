class Solution:
    '''完美数

    对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
    给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False

    我的思路：先求出它的所有正因子，然后看正因子的和是否为本身
    '''

    # 我的解法
    def check_perfect_number(self, num):
        if num <=1:   # 题目说给的正整数，测试用例里有-6.num == 1 改成num<=1
            return False

        # 求除了1 和 num本身的所有正因子
        sum = 0
        for i in range(2, int(num**0.5)+1):
            remainder = num % i
            if remainder == 0:
                sum += i + int(num/i)

        if sum+1 == num:    # 加上1因子
            return True
        else:
            return False


    # 别人的解法
    def check_perfect_number2(self, num):
        if num == 1:
            return False
        count = 1
        k = num
        i = 2
        while (i < k):
            if num % i == 0:
                count += i + num / i
            k = num / i
            i += 1
        return num == count


if __name__ == '__main__':
    s = Solution()
    print(s.check_perfect_number(28))

