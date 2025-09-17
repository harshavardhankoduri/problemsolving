#  Write a program to print the vowels in the given string and repeated  vowel should be printed only single time.  
# Testcase1 : Helloworld  
# Output : eo  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  single vowels among them are eo .  

# Testcase1 : Jacksparrow  
# Output : ao  
# Explanation : Vowels in the given string Helloworld are a,a,o . Among  them a is repeated more than once, so consider it for one time , result is  ao.
name="Helloworld"
vow="aeiouAeiou"
res=""
for i in name:
    if i in vow:
        if i not in res:
            res+=i
print(res)