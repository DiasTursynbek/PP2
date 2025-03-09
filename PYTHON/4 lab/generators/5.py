


def kemu(n):
    for i in range(n,-1,-1):
        yield i
n=int(input("put the n : "))
for ii in kemu(n):
    print(ii,end=" ")