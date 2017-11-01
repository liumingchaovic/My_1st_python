class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            query_num = target - nums[i]
            if query_num in nums:
                for a in len(nums):
                    if(nums[a] == query_num and a != i):
                        return(i, a)