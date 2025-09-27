# Problem: Write a function that removes all falsy values from an array.  Falsy values include false, 0, "", null, undefined, and NaN. 
# Testcase 1: 
# Input: [0, 1, false, 2, '', 3] 
# Output: [1, 2, 3] 
# Explanation: 
# The falsy values 0, false, and "" are removed from the array, leaving  [1, 2, 3]. 
def Remove_Falsy_Values():
    lis=[0, 1, False, 2, '', 3]
    res=[]
    for i in lis:
        if i :
            res.append(i)
    return res
print(Remove_Falsy_Values())