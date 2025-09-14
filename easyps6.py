# Write a program to check whether the digits in-between the first and last  
# digit are less than first and last digit, if yes then print true, otherwise print  false.  
# Testcase1 : 1672  
# Output : false
# Explanation : The middle digits 6,7 are not less than first digit 1 and  last digit 7 .  
# Testcase1 : 84719  
# Output : true  
# Explanation : The middle digits 4,7,1 are less than first digit 8 and last  digit 9 .
num = "84719"
first = int(num[0])
last = int(num[-1])
result = True  
for d in num[1:-1]:
    if int(d) >= first or int(d) >= last:
        result = False
        break
print(result)
