#  Write a program to print the string after removing the duplicate characters  in the string.  
# Testcase1 : madam  
# Output : d  
# Explanation : In the given string madam, the duplicates are m,a. After  removing m’s and a’s from the given string we formed a new string d.  
# Testcase1 : donkey  
# Output : donkey  
# Explanation : In the given string there is no duplicate character.  
name="donkey"
res=""
for i in name:
    if name.count(i)==1:
        res+=i
print(res)