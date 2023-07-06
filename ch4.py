#LIST METHOD'' - APPEND, SORT, REVERSE, SORT, COUNT, INDEX, EXTEND, REMOVE, POP
#LIST
a = [1,2,3,4,5]
print(a[0])
print(a[0: ])
b = [55,66,77,88]
b[0] = 99 #replacing 
print(b) 
#LIST USING []
a = [1,2,3,4,5]
print(a)
print(a[1])
print(a[4])
print(a[3])
#PRINTING DIFFERENT VALUES IN []
a = ['ESMIKA', 11, True, 22]
print(a)
#LIST SLICING
a = ['TESSA', 'HARDIN', 'ESMI', 'KIRU', 11, 55]
print(a[0:4])
print(a[-1: ])
#LIST METHOD
a = [1,92,37,4,5,66]
print(a)
a.sort() #ASSENDING ORDER
print(a)
b = [22,33,67,89,100]
b.reverse() #DESCENDING ORDER
print(b)
c = ['JAMUNA', 99, 88, 109]
c.append('CASSY') #ADDS AT THE END OF LIST
print(c)
d = [11,12,23,44]
d.insert(0, 111) #PLACING VALUE IN MIDDLE
d.insert(3,45)
print(d)
e = [1,2,3,4,8]
e.pop(0) #TO REMOVE ACC TO INDEX
print(e)
f = [77,55,67,4]
f.remove(77) #TO REMOVE THE DIGIT
print(f)

#TUPPLE
t = (1,1,2,3,4)
print(t[0])
t1 = ( ) #EMPTY TUPLE
print(t1)
t2 = (1,) #TUPLE WITH SINGLE ELEMENT
print(t2)
t3 = (2,3,4,5,7) #TUPLE WITH MANY ELEMENTS
print(t3)
t4 = (4,5,6,7,4,5,5,4) 
print(t4.count(4)) #COUNTING VALUE
print(t4.index(4)) #TO KNOW PLACEMENT 
#PRACTICE SET
a = ['APPLE', 'BANANA', 'CARROT', 'AVOCADO']
print(a)
t1 = input('ENTER THE FRUIT NAME 1 ') 
t2 = input('ENTER THE FRUIT NAME 2 ') 
t3 = input('ENTER THE FRUIT NAME 3 ') 
t4 = input('ENTER THE FRUIT NAME 4 ') 
myfruitlist = [t1,t2,t3,t4]
print(myfruitlist)
a = [55,4,1,99]
a.sort()
print(a)

t = (1,2,3,4,6)
print(t)
print(t.count(5)) #3;13;47


m1 = input('ENTER THE marks 1 ') 
m2 = input('ENTER THE marks 2 ') 
m3 = input('ENTER THE marks 3 ') 
m4 = input('ENTER THE marks 4 ') 
marks = [m1,m2,m3,m4]
marks.sort()
print(marks)
p = [1,2,3,4]
print(p[0] + p[1] + p[2] + p[3])
print(sum(p))
a = [1,2,3,4,5]
a.sort()
print(a)
b = [22,34,56,78]
b.reverse()
print(b)
c = [44,5,67,8,44]
print(c.count(44))
d = [22,5,5,5,67]
print(d.count(22))
e = (2,23,4,55,55)
print(e.count(55))
 