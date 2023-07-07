n=int(input("enter the number:"))
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end="")
    print("*"*(2*i-1),end="")
    print()
