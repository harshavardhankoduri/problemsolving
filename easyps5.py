# Write a program to check whether the sum of digits in the number except  
# first digit and digit is equal to the sum of first digit and last digit of that  number. If both the sums are equal then print equal otherwise print not  equal  
# Testcase1 : 75547  
# Output : equal  
# Explanation : In the given number 7557, first digit and last digit sum  that is sum(7,7)=14 is equal to sum of remaining numbers that is  sum(5,5,4) = 14. So both sums are equal.  
# Testcase1 : 765  
# Output : not equal  
# Explanation : Sum(7,5)=12 and Sum(6)=6, both sums are not equal.  

num = "75547"
first = int(num[0])     
last = int(num[-1])
middle_sum = 0
for i in range(1, len(num) - 1):
    middle_sum += int(num[i])
edge_sum = first + last
if edge_sum == middle_sum:
    print("equal")
else:
    print("not equal")
