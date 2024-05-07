def even_position(nums):
	for i in range(len(nums)):
		if (nums[i]%2==0 and i%2!=0) or (nums[i]%2!=0 and i%2==0):
			return False
	return True
