def Test():
	nums = []
	user_input = input("Input number seperated with comma: ").split(",")
	for length in range(len(user_input)):
		nums.append(int(user_input[length]))
	target = int(input("Input one target number"))
	for i in len(nums):
		query_num = target - nums[i]
		if query_num in nums:
			for a in len(nums):
				if(nums[a] == query_num and a != i):
					print(i, a)