# Write a program to print factorial of the number.  
# Testcase1 : 3  
# Output : 6  
# Explanation : Factorial of the number 3 is 3*2*1 = 6.  
# Testcase1 : 4  
# Output : 24  
# Explanation : Factorial of the number 4 is 4*3*2*1 = 24. 
n=3
fac=1
for i in range(1,n+1):
    fac*=i
print(fac)