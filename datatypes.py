#datatypes
i=10
print(f"integer={i},type={type(i)}")
f=1.0
print(f"float={f},type={type(f)}")
c=3+4j
print(f"complex={c},type={type(c)}")
d=True
print(f"boolean={d},type={type(d)}")
f=(10,20,30,40,50)
print(f"set={f},type={type(f)}")
g=[10,20,30,40,"tuple"]
print(f"the list={g},type={type(g)}")
h=("name:","chandana","age:",22)
print(f"dictionary={h},type={type(h)}")

#control flow
a=10
b=20
if(a<b):
    print("a is lesser then b")

a=30
b=20
if(a<b):
    print("a is lesser then b")
else:
     print("a is grater then b")

a=18
if(a<=12):
    print("a is lesser then 18")
elif(a>=30):
    print("a is greater then 18")
else:
    print("a")

#block
for i in range(10):
    i==5
    break
    print(i)

for i in range(10):
    i%2==0
    continue
    print(i)

for i in range(10):
    i==2
    pass
print(i)

#loop
for i in range(0,5):
    print(i)


