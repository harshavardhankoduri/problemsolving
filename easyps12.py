# Find the Largest Element in an Array 
# Problem: Write a function to return the largest number in an array. 
# Testcase 1: 
# Input: [3, 1, 4, 1, 5, 9] 
# Output: 9 
# Explanation: 
# In the array [3, 1, 4, 1, 5, 9], the largest number is 9. 
def lar_num():
    inpu=[3, 1, 4, 1, 5, 9]
    largenum=inpu[0]
    for i in inpu:
        if largenum<i:
           largenum=i
    return largenum
print(lar_num())
        