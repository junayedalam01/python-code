"""Functions for delete element from list in Python are:
- del
- pop()
- clear()
- remove()

Functions for update element from list in Python are:
- insert()
- append()
- extends()

All methods for deletion and upadation are explained with the help of proper examples for better understanding. Our trainer will explain it all with the help of examples and you will learn where to use which function for a smooth process in Python."""

# how to work to 'del' =======
a=[10,20,30,40,50,60,70,80,90]# index value cound 0 to ----

del a[3]
print(a)

b=[1,2,3,4,5,6,7,8,9,]
#b.pop(2) 
print(b.pop(2))
print(b)


c=[11,22,33,44,55,66,77,88,99]
c.remove(99)
print(c)

d=[111,222,333,444,555,666,777]
d.clear()
print(d)


#LIST UPDATE FUNCTION ==============

e=[21,31,41,51,61]
e[1]=10000
print(e)
#how to use " insert
f=[11,22,33,44,55,66,77]
f.insert(0,10)
print(f)
# how to use append and extend 
g=[13,14,15,16]
o=[99,00,88]
#g.append(7000)
g.extend(o)
print(g)

