
def square(a,b):
    for i in range(a,b+1):
        yield i**2
a=int(input("put the a: "))
b=int(input("put the b: "))


for ii in square(a,b):
    print(ii,end=" ")