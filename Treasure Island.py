print("""WELLCOME TO THE TREASURE ISLAND QUIZ GAME ! 
----------------------------------------------------------

Hello I'm Jarvis, your assistant on your journey to the Treasure Island! 

At start you will be left on a random island and I will assist you to the Last Island. 

Your Adventure Starts Now! \n""")

first_que = input("Which Direction You Wish To Go ?(Right or Left)\n=> ").lower()

if first_que == "left":
    
    print("\nYou are now at the shore....")
    
    sec_que = input('\nDo you want to swim or wait for a boat ? (wright "swim" or "wait")\n=> ').lower()
    
    if sec_que == "wait":
        print("\nYou crossed unharmed.\n")
        print("You are now on the treasure island....\n")
        print("There are Three Doors of color red, green & bue in front of you.\n")
        
        third_que = input('Which one you choose? (Enter "red", "green" or "blue")\n=> ').lower()
        
        if third_que == "red":
            print("Game Over! ")
        elif third_que == "green":
            print("Game Over! ") 
        elif third_que == "blue":
            print("\nYou Got The Treasure, You Won! ")
            print("\n Thanks For Playing Our Quiz Game.")
        else:
            print("You must enter an appropriate ANS.")
    elif sec_que == "swim":
        print("You were eaten by the sharks....RIP ")
    else:
        print("You must enter an appropriate ANS.")
    
elif first_que == "right":
    print("\nYou died by falling in a pit....RIP")
    
else:
    print("You must enter an appropriate ANS.")

