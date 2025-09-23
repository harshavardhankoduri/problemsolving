# Problem: Write a function that returns the sum of all elements in an array. 
# Testcase 1: 
# Input: [1, 2, 3, 4] 
# Output: 10
# Explanation: 
# The sum of the elements 1 + 2 + 3 + 4 = 10. 
def sum_of_all_elments():
    arr=[1, 2, 3, 4]
    count=0
    for i in arr:
        count+=i
    return count
print(sum_of_all_elments())