a = set()
print(type(a))
a.add(1)
a.add(4)
a.add(99)
a.add((1,2,3,4))
print(len(a))
a.remove(1)
print(a)
a ={
    'PREDATOR' : 'AUSTRALIA',
    'MUSTANG' : 'DASHAIN'
}
print(a)
a1 = {
    'family' : 'RIDE'
}
a.update(a1)
print(a)
#PRACTICE SET
a = {
    'MAYA' : 'LOVE',
    'SWORGA' : 'WEED'
}
print(a)
print('OPTIONS ARE ',a.keys())
a1 = input('ENTER YOUR WORD\n')
print('The meaning of the word is: ',a[a1])
b = set()
print(type(b))
b.add(6)
b.add(9)
b.add(8)
print(b)
d = {
    'CHABI' : 'KEY',
    'MUTU' : 'HEART'
}
print(d)
print('OPTIONS ARE', d.keys())
d1 = input('ENTER YOUR WORD\n')
print('THE MEANING OF THE WORD IS: ', d[d1])
num1 = int(input('ENTRE THE NUMBER 1\n'))
num2 = int(input('ENTRE THE NUMBER 2\n'))
num3 = int(input('ENTRE THE NUMBER 3\n'))
num4 = int(input('ENTRE THE NUMBER 4\n'))
t = {num1,num2,num3,num4}
print(t)
e = {69, '69', 69.0}
print(e)
print(len(e))
l = {}
i = input('RAM, ENTER YOUR FAVOURITE SONG : ')
j = input('SHYAM, ENTER YOUR FAVOURITE SONG : ')
k = input('MAILA, ENTER YOUR FAVOURITE SONG : ')
m = input('HARY, ENTER YOUR FAVOURITE SONG : ')
l['RAM'] = i
l['SHYAM'] = j
l['MAILA'] = k
l['HARY'] = m
print(l)
g = {}
h = input('ESMIKA, ENTER THE MUSIC THAT YOU ARE LISTENING RN\n')
i = input('KRISTINA, WHAT ARE YOU DOINg RN\n')
g['ESMIKA'] = h
g['KRISTINA'] = i
print(g)
z = {
    'HUNTED' : 'GHOST OF YOU',
    'TAKE BE BACK' : 'THE NIGHT WE MET'
}
print(z)
x = {
    'MISS YOU' : 'ESMIKA'
}
z.update(x)
print(z)
l = {
    'BARSHA' : 'MAINA',
    'FAST' : 'CHITO'
}
print(l)
f = {
    'THOUSAND' : 'SAI'
}
l.update(f)
print(l)