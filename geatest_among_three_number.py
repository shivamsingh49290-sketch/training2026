year=int(input("Enter Any Year"))
print("Year=",year)

if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("not leap year")
elif year%4==0:
    print("leap year")
else:
    print("not leap year")
