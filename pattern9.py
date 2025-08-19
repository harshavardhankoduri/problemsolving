
def star_pattern(n, limit):
    if n <= limit:
        print("*" * n)
        star_pattern(n + 1, limit) 

star_pattern(1,5)
n=1
if n==1:
    print("*")
    n+= 1
    if n==2:
        print("*"*2)
        n+= 1
        if n==3:
            print("*"*3)
            n+= 1
            if n==4:
                print("*"*4)
                n+= 1
                if n==5:
                    print("*"*5)
else:
    print("Invalid input")


