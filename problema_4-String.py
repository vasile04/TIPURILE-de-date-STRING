a=str(input("primul cuvant: "))
b=str(input("al doilea cuvant: "))
c=str(input("al treilea cuvant: "))
d=str(input("al patrulea cuvant: "))
l=str(a)
m=str(b)
n=str(c)
o=str(d)
q=0
if(((len(m))>=3)and((len(o))>=3)and((len(l))>=3)and((len(n))>=3)):
    q=(len(o))/2
    i=int(q)
    j=l[:2]
    k=m[0]
    h=n[:3]
    g=o[:i]
    print(a,b,c,d, sep="  ")
    print(str(j)+str(k)+str(h)+str(g))
else:
    print("nu corespunde conditiei")

