n=int(input("Enter number of terms : "))
n1=0
n2=1
count=0
if n<=0:
    print("Please enter a positive integer !!")
elif n==1:
    print("Fibonacci Series upto",n,":")
    print(n1)
else:
    print("Fibonacci Series upto",n,":")
    while(count<=n):
        print(count)
        n1=n2
        n2=count
        count=n1+n2
