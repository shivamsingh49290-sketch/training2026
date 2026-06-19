def person(age=18,name='chor'):
    age=age+10
    print("name=",name,"age=",age)

# 1.positional argument passing
#person("Ram",22)
#person(22,"ram")

# 2.keyword argument passing
person(name='Ram',age=66)
person(age=55,name='rohan')

#3. variable length argument
# def add(x,*y):
#     #s=x+y
#     print("x=",x)
#     print("y=",y)
#     s=x
#     for i in y:
#         s=s+i
#     return s
#
# print(add(66,99,666,88,666,99,66,6,12,5,6))
def add(*y):
    print("y=",y)
    s=0
    for i in y:
        s=s+i
    return s

print(add(66,99,666,88,666,99,66,6,12,5,6))

# 4. keyword variablelength argument
def persondata(**data):
    print(data)

persondata(name='ram',age=50,phone=66969969,pin=563998)

person(name='rohan')
person()