#SNAKE_WATER_GUN
import random
def gamewin(comp,you):
    if comp == you:
       return None
    elif comp == 's':
       if you == 'w':
          return False
       elif you == 'g':
          return True
       elif comp == 'w':
          if you =='g':
             return False
          elif you == 's':
             return True
          elif comp == 'g':
             if you == 's':
                return False
             elif you == 'w':
                return True
print('comp turn: snake(s) water(w) or gun(g)?')
randNO = random.randint(1,3)

if randNO == 1:
   comp = 's'
elif randNO == 2:
  comp = 'w'
elif randNO == 3:
  comp = 'g'
you = input('My turn: snake(s) water(w) or gun(g)?')
a = gamewin(comp,you)
print(f"Computer choose {comp}")
print(f"You choose {you}" )
if a == None:
   print('THE GAME IS A TIE!')
elif a:
   print('You win!')
else:
   print('YOU LOSE!')
 #ROCK_PAPER_SCISSOR
import random
def gamewin(com,me):
   if com == me:
    return None
   elif com == 'r':
      if me == 'p':
         return 'True' 
      elif me == 's':
         return False
   elif com == 's':
     if me == 'p':
        return False
     elif me == 'r':
        return True
     elif com == 'p':
        if me == 's':
           return True
        elif me == 'r':
           return False
   
print('Com turn: rock(r), paper(p), sicssor(s)')
randomno = random.randint(1,3)

if randomno == 1:
   com = 'r'
elif randomno == 2:
   com = 'p'
elif randomno == 3:
   com = 's'
me = input('My turn: rock(r), paper(p), scissor(s)')
b = gamewin(com,me)
print(f"Computer chose {com}")
print(f"You chose {me}" )
if b == None:
  print('The game is Tie!')
elif b:
   print('YOU WON THE FUCKIIN GAME')
else:
   print('BAD LUCK, YOU LOSE IT AS YOUR EX')




