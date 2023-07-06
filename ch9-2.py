#MULTIPLICATION from:2-20,

for i in range (1,21):
 with open (f'3table.txt', 'w') as f:
   for j in range(1,11):
    f.write(f'{i}*{j}={i*j}\n')   
     

 