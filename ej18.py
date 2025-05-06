def buildArray(nums):
        ans = []

        for i in range(len(nums)):
            ans += [nums[nums[i]]]

        return ans