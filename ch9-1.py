def game():
    return 99996
score = game()
with open('justin2.txt') as f:
 a = int(f.read())
if a<score:
   with open ('justin2.txt', 'w') as f:
     f.write(str(score))


#NEWLY
def game():
   return 4444
num = game()
with open('justin2.txt', 'r') as f:
   a = f.read()
if a == '':
    with open('justin2.txt', 'w') as f:
      f.write(str(num))
elif int(a<num):
  with open ('justin2.txt', 'w') as f:
    f.write(str(num))

