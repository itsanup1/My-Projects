size = input("Which Pizza do you want ? (S, M or L) ")
add_pepperoni = input("Want some add_pepperoni ? (Y or N) ")
extra_cheese = input("Want to add extra cheese ? (Y or N) ")
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L" :
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
else:
    print("pls enter a valid ans ! ")
if extra_cheese == "Y" :
    bill += 1               
print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}")