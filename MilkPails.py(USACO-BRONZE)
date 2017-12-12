o= open("pails.in","r")
o2=open("pails.out","w")

l=[]
f=[]

for i in o:
    d=list(i.split(' '))

for v in d:
    v=int(v)
    l.append(v)

x=int(l[0])
y=int(l[1])
m=int(l[2])
ox=x
oy=y
rand=1

if m%x == 0 or m%y == 0 or ((m%y)%x)==0 or ((m%x)%y)==0:
    o2.write(str(m))

else:
    while y*rand<=m:
        f.append(y*rand)
        rand+=1

    while x*rand<=m:
        f.append(x*rand)
        rand+=1

    while x+y<=m:
        sum=x+y
        f.append(sum)
        y+=oy
        if x+y>m:
            x+=ox
            y=oy

    if not f:
        o2.write(str(y))
    else:
        o2.write(str(max(f)))
print f
