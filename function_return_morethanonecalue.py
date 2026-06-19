def calci(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return add,sub,mul,div

a=int(input("enter first Number"))
b=int(input("enter second Number"))

p,q,r,s=calci(a,b)
print(p,q,r,s)