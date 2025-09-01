# Write a program to print middle character(s) in the given string or 
# number.  
# Testcase1 : Wonder  
# Output : nd  
# Explanation : The middle characters in the given word Wonder is nd.  
# Testcase1 : World  
# Output : r  
# Explanation : The middle character in the given word World is r.  Test Case 1 : 6969  
# Output : 96  
# Explanation : The middle character in the given number 6969 is 96. 
str = "wonder"
length = len(str)
res = ""
for i in range(length):
    if length % 2 ==0:
        if i == length//2-1 or i == length//2:
            res+=str[i]
    else:
        if length%2 ==1:
            if i==length//2:
                res+=str[i]
print(res)
