def missingInteger(self, nums):
        if len(nums) == 1:
            return nums[0]+1

        index = 1
        lsps = nums[0]

        while index < len(nums) and nums[index] == (nums[index-1] + 1):
            lsps+=nums[index]
            index += 1

        while lsps in nums:
            lsps += 1

        return lsps