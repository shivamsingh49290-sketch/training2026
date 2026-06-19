x=100

def msg():
    x=10
    global y
    y=6666
    print("Local x=",x)

msg()
print("X=",x)
print("Y=",y)