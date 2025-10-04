# Remove Vowels from a String
# Question: Write a function to remove all vowels from a given string.
# Testcase: "hello world"
# Output: "hll wrld"
# Explanation: After removing the vowels 'e', 'o', and 'o' from "hello world", we are left with "hll wrld".
def Vowels_in_a_String():
    name="hello world"
    vowels="aeiouAEIOU"
    res=""
    for i in name:
        if i not in vowels:
            res+=i
    return res
print(Vowels_in_a_String())