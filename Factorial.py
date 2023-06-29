num=int(input("Enter a number to find factorial : "))
n=1
fact=1
while(n<=num):
    fact=fact*n
    n+=1
print("Factorial of ",num," is ",fact)