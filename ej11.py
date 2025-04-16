nums = [2,7,11,15]
target = 9

def twosum(nums, target):

    visited = {}

    for i in range(len(nums)):
        
        cur = nums[i]
        x = target - cur

        if(x in visited.keys()):
            return [i, visited[x]]
        else:
            visited[cur]=i
    return 0

twosum(nums, target)