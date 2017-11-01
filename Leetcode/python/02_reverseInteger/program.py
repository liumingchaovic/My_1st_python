class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in range(-2**31, 2**31-1):
            if x > 0:
                x_reverse = int(str(x)[::-1])
                if x_reverse in range(-2*31, 2**31-1):
                    return x_reverse
                else:
                    return 0
            else:
                x_abs = abs(x)
                x_abs_reverse = int(str(x_abs)[::-1])
                if -x_abs_reverse in range(-2**31, 2**31-1):
                    return -x_abs_reverse
                else:
                    return 0
        else:
            return 0


