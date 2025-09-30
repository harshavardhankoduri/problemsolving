# Question: Write a function to reverse a given string.
# Testcase: "hello"
# Output: "olleh"
# Explanation: The reverse of the string "hello" is "olleh". Each character's order is reversed.
def Reverse_a_String():
    name= "hello"
    res=""
    for i in name:
        res=i+res
    return res
print(Reverse_a_String())
