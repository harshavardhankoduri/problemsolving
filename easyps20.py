# Problem: Write a function that returns the sum of all even numbers in an  array. 
# Testcase 1: 
# Input: [1, 2, 3, 4, 5] 
# Output: 6 
# Explanation:
# The even numbers in the array are 2 and 4. Their sum is 2
def Sum_of_Even_Numbers():
    lis=[1, 2, 3, 4, 5]
    sumofeven=0
    for i in lis:
        if i%2==0:
            sumofeven+=i
    return sumofeven
print(Sum_of_Even_Numbers())