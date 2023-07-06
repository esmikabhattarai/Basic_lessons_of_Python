
#from playsound import playsound
#playsound("C:\\Users\\user\\Downloads.mp3")

post = input('ENTER A NAME\n')
if 'esmi' in post:
  print('POST IS TALKING ABOUT ESMI')
elif ' ESMI'in post:
  print('POST IS TALKING ABOUT ESMI')
else:
  print('POST IS NOT TALKING ABOUT ESMI')
  def beautiful(name):
   print('WOW ' + (name))
  beautiful('ESMIKA')
def add(num1, no2):
  return num1+no2
b = add(2,3)
print(b)
def country(name):
  print('WELCOME TO '+ (name))
  country('SUCKS')

  def average(k,e):
    print('THE AVG IS ', (k+e)/2) 
  average(5,15)
  def average(a,b,c=3):
    print('THE VALUE is ',(a+b+c)/2)
  average(a=2)
  average(b=4)