a=4
b=5
print(b,b-2,b-1)
m = 4
n = 77
print(m,n-5,n*5)
a = None
if (a is None):
    print('YES')
else:
    print('NO')
a = int(input('ENTER A CUTE NUMBER '))
if(a>10):
 print('YES')
else:
   print('NO')
k = [1,2,3,45]
print(2 in k)
print(7 in k)
z = {2,3,4,566,7}
print(2 in z)
print(8 in z)
l = 55
if(l==55):
   print('FINE')
elif(l>66):
   print('no and yes')
#PRACTICE SET
a = int(input('ENTER FOUR NUMBER '))
a1 = int(input('ENTER FOUR NUMBER '))
a2 = int(input('ENTER FOUR NUMBER '))
a3 = int(input('ENTER FOUR NUMBER '))
if(a>a3):
  f1=a
else:  
  f1=a3
if(a1>a3):
  f2=a1
else:
  f2=a2 
if(f1>f2):
 print(str(f1) + ' is greatest')
else:
 print(str(f2) + ' is greatest')
 eng = int(input('ENTER YOUR MARKS '))
 sci = int(input('ENTER YOUR MARKS '))
 opt = int(input('ENTER YOUR MARKS '))
if(int(eng<33 or sci<33 or opt<33)):
  print('YOU ARE FAILED BCZ YOU HAVE 33% IN ONE SUB')
elif(int(eng+sci+opt)/3 <40):
 print('YOU ARE FAIL DUE TO LESS PER i.e 40%')
else:
 print('YOU HAVE PASSED')
b1 = int(input('ENTER THE NUMBER '))
b2 = int(input('ENTER THE NUMBER '))
if(b1>b2):
  print('The greatest number is b1')
else:
  print('The greatest number is b2')
d = input('ENTER THE TEXT ')
if('USA'):
  spam = True
elif('Australia'):
 spam = True
elif('Finland'):
 spam = True
else:
 spam = False
if(spam):
  print('THIS IS SPAM')
else:
  print('This is not spam')
character = 'ESMIKAISAGOODGIRL'
character.count()
if(character<10):
  print('Character is less than 10')
else:
  print('Character is more than 10')