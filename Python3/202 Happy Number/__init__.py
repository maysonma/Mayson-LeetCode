class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(num):
            next_num = 0
            q = num
            while q > 0:
                r = q % 10
                q = q // 10
                next_num += r ** 2
            return next_num

        fast = slow = n
        while fast != 1 and cal(fast) != 1:
            fast = cal(cal(fast))
            slow = cal(slow)
            if fast == slow:
                return False

        return True
