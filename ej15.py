nums = [-1,0,3,5,9,12]
target = 15

def search(nums, target):

    if len(nums) == 0:
            return False

    mid = len(nums)//2

    if(nums[mid] == target):
        return True
    elif(nums[mid] < target):
        return search(nums[mid+1:], target)
    return search(nums[:mid], target)

print(search(nums, target))