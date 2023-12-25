def fact(x):
    f=1
    i=1
    while i<=x:
        f=f*i
        i+=1
    return f
def per(n,r):
    num=fact(n)
    den=fact(r)
    ans=num//den
    return ans
def comb(n,r):
    num=fact(n)
    den=fact(r)
    den=fact(n-r)*den
    ans=num//den
    return ans
n=int(input("enter n"))
r=int(input("enter r"))
perm=per(n,r)
com=comb(n,r)
print(perm)
print(com)
