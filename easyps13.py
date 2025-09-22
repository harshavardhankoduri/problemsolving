# Problem: Write a function to return the second largest number in an array. 
# Testcase 1: 
# Input: [3, 1, 4, 1, 5, 9] 
# Output: 5 
# Explanation: 
# In the array [3, 1, 4, 1, 5, 9], the second largest number after 9 is 5. 
def second_largest(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None  
    unique_nums.sort(reverse=True)   
    return unique_nums[1]
print(second_largest([3, 1, 4, 1, 5, 9]))
