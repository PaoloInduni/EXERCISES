nums = [7,8,3,4,15,13,4,1]

def minimumAverage(nums):
    
    averages = []
    cicles = len(nums) // 2

    nums.sort()

    for i in range(cicles):
        averages.append((nums[i] + nums[~i])/2)

    return min(averages)

print(minimumAverage(nums))
