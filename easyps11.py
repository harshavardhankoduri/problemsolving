#  Write a program to print all the Upper case letters in the string in reverse  order and then followed by the lower case letters .  
# Testcase1 : NumberOne  
# Output : ONumberne  
# Explanation : In the given string NumberOne, Uppercase letters are N,O.  The reverse order of them are ON next it is followed by lowe case letters  (umberne). So final string is ONumberne.
# Testcase1 : ClassLeader  
# Output : LClasseader  
# Explanation : In the given string ClassLeader, Uppercase letters are C,L.  The reverse order of them are LC next it is followed by lowe case letters  (lasseader). So final string is LClasseader. 
name="ClassLeader"
res=""
for i in name:
    if i.isupper():
        res=i+res
    else:
        res+=i
print(res)