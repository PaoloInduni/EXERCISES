nums = [3,3]
target = 6

def twoSum(nums, target):
        
        visited = {}

        for index in range(len(nums)):
            if visited.__contains__(target-nums[index]):
                return [visited[target-nums[index]], index]
            else:
                visited[nums[index]] = index
                
        return False
    
print(twoSum(nums, target))