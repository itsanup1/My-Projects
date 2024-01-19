import random as rd
start = input('To Flip the coin Hit "Enter" ')
result = rd.randint(1,2)
if result == 1:
    print('''You got HEAD!
  ---
|  O  |
  ---''')
else:
    print('''You goy TAIL!
   ---
|   l   |
   --- ''')