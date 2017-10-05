class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print('nums you input is %s' % nums)
        print('target you input is %d' % target)
        m = 0
        for m in list(range(0, len(nums), 1)):
            for n in list(range(m + 1, len(nums), 1)):
                target_test = nums[m] + nums[n]
                if target_test == target:
                    print("nums[%d] + nums[%d] = %d" % (m, n, target))
                    return m, n
if __name__ == '__main__':
    nums = []
    a = input('Please input list nums:')
    for i in a.split(','):
        nums.append(int(i))
    target = int(input('Please input target:'))
    slt = Solution()
    slt.twoSum(nums, target)
