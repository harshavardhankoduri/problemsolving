# Question: Write a function to count the number of vowels in a given string.
# Testcase: "hello world"
# Output: 3
# Explanation: The vowels in "hello world" are 'e', 'o', and 'o'. Thus, the total count of vowels is 3.
def Vowels_in_a_String():
    name="hello world"
    vowels="aeiouAEIOU"
    count=0
    for i in name:
        if i in vowels:
            count+=1
    return count
print(Vowels_in_a_String())