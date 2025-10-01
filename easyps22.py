# Check if a String is a Palindrome
# Question: Write a function to check if a given string is a palindrome.
# Testcase: "racecar"
# Output: true
# Explanation: A palindrome is a string that reads the same forward and backward. Since "racecar" is the same in both directions, the output is true.
def String_is_a_Palindrome():
    string="racecar"
    str2=""
    for i in range(len(string)-1,-1,-1):
        str2+=string[i]
    if string==str2:
            return True
    return False
print(String_is_a_Palindrome())     