# Problem: Write a function to check if an array is sorted in ascending  order.  
# Testcase 1: 
# Input: [1, 2, 3, 4, 5] 
# Output: true 
# Explanation: 
# The array [1, 2, 3, 4, 5] is sorted in ascending order. 
def  Array_is_Sorted():
    arr=[1, 2, 3, 4, 5]
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
print(Array_is_Sorted())
