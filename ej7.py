nums = [3,2,2,3]
val = 3

def removeElement(nums, val):
        
        i = 0
        k = 0
        length = len(nums)
        
        while i < length:
            if nums[i] == val:
                nums.pop(i)
                length -= 1
                continue
            k += 1
            i += 1

        return nums

print(removeElement(nums, val))