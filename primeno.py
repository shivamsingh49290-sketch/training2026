n=int(input("enter any number"))
i=2
while i<n:
    if n%i==0:
        print(" not prime no")
        break
    i=i+1
else:
    print("prime no")