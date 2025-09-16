# Write a program to print the vowels in the given string in reverse order.  
# Testcase1 : Helloworld  
# Output : ooe  
# Explanation : Vowels in the given string Helloworld are e,o,o . The  reverse order of eoo is ooe.  
# Testcase1 : JackspArrow  
# Output : oAa  
# Explanation : Vowels in the given string JackspArrow are a,A,o . The  reverse order of aAo is oAa.  
nam="JackspArrow"
vow="aeiouAeiou"
res=""
for i in nam:
    if i in vow:
        res=i+res
print(res)