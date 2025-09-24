# Problem: Write a function to remove duplicate values from an array. 
# Testcase 1: 
# Input: [1, 2, 2, 3, 4, 4, 5] 
# Output: [1, 2, 3, 4, 5] 
# Explanation: 
# The duplicates 2 and 4 are removed from the array, leaving [1, 2, 3,  4, 5]. 
def remove_duplicate_values():
    arr=[1, 2, 2, 3, 4, 4, 5]
    res=[]
    for i in arr:
        if i not in res:
            res.append(i)
    return res
print(remove_duplicate_values())