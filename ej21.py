def findPrefixScore(nums):
        count = 0
        highest = 0
        conver = []
        for i in range(len(nums)):
            if nums[i] > highest:
                highest = nums[i]
            count+=nums[i]+highest
            conver.append(count)
        return conver