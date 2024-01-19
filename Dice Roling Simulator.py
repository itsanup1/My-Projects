import random
print("WELCOME TO THE DICE ROLING SIMULATOR !")

input('\nTo Role A Dice Hit "Enter"! ')

result= random.randint(1,6)

if result == 6:
    print('''
+-------+
| O   O |
| O   O |
| O   O |
+-------+''')
if result== 5:
    print('''
 +-------+
| O     O |
|    O    |
| O     O |
 +-------+
''')
if result == 4:
    print('''
 +-------+
| O     O |
|         |
| O     O |
 +-------+''')
if result == 3:
    print('''
+-------+
|     O |
|   O   |
| O     |
+-------+''')
if result == 2:
    print('''
+-------+
|     O |
|       |
| O     |
+-------+''')
if result == 1:
    print('''
+-------+
|       |
|   O   |
|       |
+-------+''')

print(f"\nYou got {result} !")