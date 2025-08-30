# Write a program to print reverse of the given number.  
# Testcase1 : 721  
# Output : 127  
# Explanation : Reverse of the number 721 is 127.  
# Testcase1 : 765  
# Output : 567  
# Explanation : Reverse of the number 765 is 567. 
a=input("enter the number:")
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
print(b)