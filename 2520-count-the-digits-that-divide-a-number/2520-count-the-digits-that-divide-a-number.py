class Solution(object):
    def countDigits(self, num):
        count = 0
        n = num

        while n > 0:
            digit = n % 10

            if num % digit == 0:
                count += 1

            n = n // 10

        return count