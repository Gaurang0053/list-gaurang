"""
#eval func
list=eval(input("Enter List:"))
print(list)
print(type(list))

#list func
l=list(range(0,10,2))
print(l)
print(type(l))

#split func
s="Learning Python is very very easy !!!"
l=s.split()
print(l)
print(type(l))

#slicefunc
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
print(n[4:100])

#mutable
n=[10,20,30,40]
print(n)
n[1]=777
print(n)

#while loop
n=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(n):
 print(n[i])
 i=i+1

#for loop
n=[0,1,2,3,4,5,6,7,8,9,10]
for n1 in n:
   print(n1)

# reverse():
#We can use to reverse() order of elements of list.
n=[10,20,30,40]
n.reverse()
print(n)

#sort
n=[20,5,15,10,0]
n.sort()
print(n)
"""
