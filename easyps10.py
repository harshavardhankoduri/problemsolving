#  Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa.  
# Testcase1 : JohnWick  
# Output : jOHNwICK  
# Explanation : All the upper case letters changed to lower case and vise  versa.  
# Testcase1 : Korean  
# Output : kOREAN  
# Explanation : All the upper case letters changed to lower case and vise  versa.
con="JohnWick"
result=""
for i in con:
    if i.islower():
        result+=i.upper()
    else:
        result+=i.lower()
print(result)