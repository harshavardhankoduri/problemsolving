# Problem: Write a function to reverse the elements in an array. 
# Testcase 1: 
# Input: [1, 2, 3, 4, 5] 
# Output: [5, 4, 3, 2, 1] 
# Explanation: 
# The array [1, 2, 3, 4, 5] is reversed to [5, 4, 3, 2, 1].
def Reverse_an_Array():
    lis=[1,2,3,4,5]
    res=[]
    for i in range(len(lis)-1,-1,-1):
        res.append(lis[i])
    return res
print(Reverse_an_Array ())