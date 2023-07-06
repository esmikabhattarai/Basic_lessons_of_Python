d#LOOP
a = 5
while a<10:
    print('ESMI' + str(a))
    a = a + 1

b = 15
while b>10:
    print('SUCCESS' + str(b))
    b = b - 1
print('DONE')

c = 1
while c<=50:
    print(c)
    c = c + 1

d = 0
while d<6:
 print('RONALDO')
 d = d + 1
 
falful = ['SYAU', ' ANGUR', 'AMBAK', 'KATAR']
i = 0
while i<len(falful):
   print(falful[i])
   i = i + 1

makeupkit = ['MOISTURIZER', 'FOUNDATION', 'BLUSH', 'EYELINER','CONSILER']
i = 0
while i<len(makeupkit):
   print(makeupkit[i])
   i = i + 1
 
#FOR LOOP
fruits = ['BANAN','APPLE','WATERMELON', 'GRAPES']
for item in fruits:
 print(item)

 for i in range(0,10):
    print(i)

for e in range(1,10,2):
   print(e) #STEP-SIZE

for k in range(10):
   print(k)
else:
   print('THESE ARE THE NUMBER')

#BREAK
for t in range(8):
   print(t)
   if t == 5:
      break
#CONTINUE
for g in range(10):
    if g == 5:
      continue
print(g)
for k in range(7):
   if k == 6:
       continue
   print(k)
   #PRACTICE
num = int(input('ENTER THE NUMBER '))
for i in range(1,11):
    print(str(num) + '*' + str(i) + '=' + str(i*num))
a = int(input('ENTER THE NUMBER '))
for i in range (0,5):
   print(str(a) + '+' + str(i) + '=' + str(a+i))
b = ['MAKWANKUR','KANXI','SAJJAN', 'KALEGI','ESMI']
for name in b:
   print(name)
   if name.startswith('K'):
      print('BITCH ' + name)  

c = int(input('ENTER A NUMBER\n'))
prime=True
for i in range(1,c):
   if(c%i == 0):
      prime=False
      break 
if  prime:
      print('THIS IS A PRIME NUM')
else:
   print('THIS IS NOT A PRIME NUMBER')
   #find the prime number-unsuccessful

z = int(input('ENTER THE NUMBER '))
for i in range(0,5):
   print(str(z) + '+' + str(i) + '=' + str(z+i))

for i in range(5):
  print('*' *i)

a = int(input('ENTER THE NUMBER '))
for i in range(1,11):
 print(str(a)+'*'+str(i)+'='+str(a*i))
 z = ('   *   ')
 Z1= ('  ***  ')
 ZA2= (' **** ')
 a = int(18)
print(a*3)
#n! = 1*2*3*4*.......*n
#5! = 1*2*3*4*5
j = int(input('ENTER THE NUM '))
factorial = 1
for i in range(1, j+1):
   factorial = factorial *i
   print(f'THE FACTORIAL OF THIS {j} IS {factorial }')
k = 4
for i in range(4):
   print('*' * (i*4))
   g = int(input('ENTER THR NUMBER\n'))
   for i in range(10,0,-1): #to print reverse multiplication
      print(f"{g}*{i}={g*i}")
      #print(a*i)
     
            