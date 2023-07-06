#FUNCTIONS AND RECURSION
def percent(marks):
 return(sum(marks)/400)*100
marks1 = [98,99,78,40]
percentage1 = percent(marks1)
marks2 = [33,54,19,37]
percentage2 = percent(marks2)
print( percentage1 , percentage2)
def greet(name):
  print('Goodmorning ' + (name))
greet('ESMIKA')

def respect(name): 
  print('HELO ' + (name))
respect('ESMI')
def multiply(no1, no2):
  return no1*no2
a = multiply(2,3) 
print(a)
def beautiful(name):
  print('WOW' + (name))
beautiful('ESMIKA')
def add(num1, no2):
  return num1+no2
b = add(2,3)
print(b)
def country(name='USA'): #DEFALUT PARAMETER/VALUE/ ARGUMENT
  print('WELCOME TO '+ (name))
country('SUCKS')
country()
def country(name='Germany'):
  print('THE COUNTRY IM GOING IS ,' + (name))
country("WELCOME")
country()
n = 6
product = 1
for i in range(n):
  product = product * (1+i)
  print(product)
def factorial_iter(n):
  product = 1
  for i in range(n):
     product = product * (i+1)
  return product
#n! = 1*2*3*4*5.......*n
#n! = [1*2*3*4*5....n-1]*n
#n! = (n-1)! * n   
n = 5
product = 1
for i in range(n):
  product = product * (i+1)
  print(product) #FINDING FACTORIAL
k = 7
product = 1
for i in range(n):
  product = product *(i+1)
  print(product)
  def factoprial_iter(n):
    product = 1
    for i in range(n):
      product = product *(i+1)
      return product
print(factorial_iter(5))
#INSTEAD OF WRITING PRINT /f = , print(f)
def factorial_recursive(n):
  if n==0 or n==1: 
    return 1
  return n* factorial_recursive(n-1)
print(factorial_recursive(5))
def factorial_recursive(n):
  if n == 1 or n == 0:
    return 1
  return n * factorial_recursive(n-1)
f = factorial_recursive(5)
print(f)

def average(k,e):
  print('THE AVG IS ', (k+e)/2) 
average(5,15)
#PRACTICE
def maximum(num1,num2,num3):
  if (num1>num2):
    if(num1>num3):
      return num1
    else:
      return num3
  else:
    if (num2>num3):
    
        return num2 
    else: 
        return num3
a = maximum(5,6,7)
print('THE VALUE OF MAXIMUM NUM IS ' + str(a))
def minimum(no1,no2,no3):
  if (no1<no2):
    if(no1<no3):
      return no1
    else:
      return no2
  else:
    if (no2<no3):
      return no2
    else:
      return no3
b = minimum(88,33,55)
print('THE MINIMUM VALUE IS ' + str(b))
def ferh(cel):
  return (cel* (1.8)) + 32
c = 55
f = ferh(c)
print('THE Ferh is ' + str(f))

def ferh(cel):
  return (cel * (1.8)) + 32
cel = 33
f = ferh(cel)
print('THE FARH IS ' + str(f))

def BABE(name='ESMI'):
 print ('The name of your cute babe is ' + (name))
BABE('ok')
BABE()

print('ESMIKA', end=' ')
print('HAVE', end=' ')
print('A', end=' ')
print('GREAT', end=' ')
print('PYTHON', end=' ')
print('COMMAND', end=' ')
 
#TO FIND SUM OF giVEN NATURAL  NUM GIVEN BTY USER
#INCORRECT / CORRECT
def f_r(n):
  if n==0 or n==1:
    return(n)
  else:
    return n + f_r(n-1)
num = 8
if num<0:
  print("IT'S A POSITIVE NUMBER")
else:
  print('the sum is ',f_r(num))

n = 8
for i in range (n):
  print('*' * (n-i))
def cm(inches):
 return (inches * 2.54)
inches = 44
c = cm(inches)
print('The cm is ' + str(c))  
def mins(day):
  return (day*12*60)
day = 5
m = mins(day)
print('The minutes is ' + str(m))
a = int(input('enter a number '))
for i in range(1,11):
  print(str(a) + '*'+ str(i) +'=' + str(a*i))