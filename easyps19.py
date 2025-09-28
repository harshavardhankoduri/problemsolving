# Problem: Write a function to find the unique elements in an array  (elements that appear only once). 
# Testcase 1: 
# Input: [1, 2, 2, 3, 4, 4, 5] 
# Output: [1, 3, 5] 
# Explanation: 
# The unique elements that appear only once in the array are 1, 3, and 5. 
def find_unique_elements():
    arr = [1, 2, 2, 3, 4, 4, 5]
    res = []
    for i in arr:
        if arr.count(i) == 1:
            res.append(i)
    return res
print(find_unique_elements())