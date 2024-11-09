a = "Mmama's Boy, "

b = 'MAMA"S GIRL'

c = a + b 
print(c)
k = 22
l = 33
c = k + l 
print(c)
print('HELLO')
a = 77
b = 666
print(a + b)
a = input('My name is: ')
print(type(a))
a = 7
b = 8
c = (a + b)
print(c)
a = 33
b = 65
print(a>b)
bool1 = True
bool2 = False
print('The value of bool1 and bool2 is ',(bool1 and bool2) )
print( '''WARI JAMUNA 
           PARI JAMUNA JAMUNA KO FEDA MA MANAKAMANA''')
a = '888'
a = int(a)
print( a + 5)
a = 22
a +=6
print(a)
# STRING SLICING
a = 'HARRY'
print(a[2])
babe = 'ESMIKA'
print(babe[4])
print(babe[0:5])
k = 'kisme'
print(k[0:4])
print(k[:3])#is same as [0:3]
print(k[0:])#is same as [0:4] 
#NEGATIVE INTEGER
a = 'ESMIISACODER'
print(a[-6:-1])
print(a[1:7:2])
print(a[2:8:3])
#STRING WITH SKIP VALUE
p = 'JASMINEFLOWER'
print(p[1:6:2])
print(p[0::3])
z = 'hypothesis'
print(z[3::1])
print(z[1::2])
#STORY FUNCTION
song = ('''when I look into your eyes
I can see a love restrained
But, darlin', when I hold you
Don't you know I feel the same? Yeah...
'Cause nothing lasts forever
And we both know hearts can change
And it's hard to hold a candle
In the cold November rain''')
print(len(song))
print(song.endswith('November'))
print(song.endswith('rain'))
print(song.count('u'))
print(song.count('a'))
print(song.capitalize())
print(song.find('love'))
print(song.replace('love', 'ESMIKA'))
#ESCAPE SEQUENCE
music = "Seasons change and our love went cold. \nFEED the flame 'cause we can't let go"
print(music)
#LIST
a = [1,2,3,4,5]
print(a[0])
print(a[0: ])
b = [55,66,77,88]
b[0] = 99
print(b)