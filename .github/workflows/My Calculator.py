
import math as m

print("\nCalculator By its_anup")

undersc = "_"

print(str(undersc)*45)

print()

print("1. Add \n2. Substract \n3. Multiply    \n4. Divide \n5. Find Square of \n6. Find Squareroot of  \n7. Find Perimeters of \n8. Find Area of \n9. Tables")

print(str(undersc)*45)

print()

operation = input('Which Number of Operation Do You Want : ')

if operation == "1":

    print(str(undersc)*45)

    print()

    num1 = input("Enter Your 1st Num : ")

    num2 = input("Enter Your 2nd Num : ")

    print("The Ans Is : " + str(int(num1)+        int(num2)))

elif operation == "2":

    print(str(undersc)*45)

    print()

    num1 = input("Enter Your 1st Num : ")

    num2 = input("Enter Your 2nd Num : ")

    print("The Ans Is : " + str(int(num1)-     int(num2)))

elif operation == "3":

    print(str(undersc)*45)

    print()

    num1 = input("Enter Your 1st Num : ")

    num2 = input("Enter Your 2nd Num : ")

    print("The Ans Is : " + str(int(num1)*           int(num2)))

elif operation == "4":

    print(str(undersc)*45)

    print()

    num1 = input("Enter Your 1st Num : ")

    num2 = input("Enter Your 2nd Num : ")

    print("The Ans Is : " + str(int(num1)/int(num2)))

elif operation == "5":

	  print(str(undersc)*45)	  print()

	  num1 = int(input("Enter Your Num : "))

	  print(m.pow(num1,2))

elif operation == "6":

  	print(str(undersc)*45)

  	print()

  	num1 = int(input("Enter Your Num : "))

  	print(m.sqrt(num1))

elif operation == "7":

    print(str(undersc)*45)

    print()

    print("1. Circle \n2. Square \n3. Rectangle \n4. Triangle")

    

    cir = input("Which Num Of Perimeter do you want to find : ")

    

    if cir == "1":

      print(str(undersc)*45)

      print()

      r = int(input("\nEnter Radius of Circle : "))

      print(f"The Answer Is : {2*m.pi*r}")

      

    if cir == "2":

      print(str(undersc)*45)

      print()

      side = int(input("Enter Side of Square : "))

      print(f"The Answer Is : {side*4}")

      

    if cir == "3":

      print(str(undersc)*45)

      print()

      side1=int(input("Enter Length : "))

      side2=int(input("Enter Widgth : "))

      print(f"The Answer Is : {side1+side1+side2+side2}")

    

    if cir == "4":

      print(str(undersc)*45)

      print()

      side1=int(input("Enter Length 1st Side : "))

      side2=int(input("Enter Length 2nd Side : "))

      side3=int(input("Enter Length 3rd Side : "))

      print(f"The Answer Is : {side1 + side2 +side3}")

elif operation == "8":

  print(str(undersc)*45)

  print()

  print("1. Circle \n2. Square \n3. Rectangle \n4. Triangle")

  ar = input("\nWhich No of Area You Want to Find : ")

  

  if ar == "1":

    print(str(undersc)*45)

    print()

    r = int(input("Enter Radius : "))

    print(f"The Answer Is : {m.pi*m.pow(r,2)}")

  

  if ar == "2":

    print(str(undersc)*45)

    print()

    side = int(input("Enter Your Side : "))

    print(f"The Answer Is : {m.pow(side,2)}")          

  if ar == "3":

    print(str(undersc)*45)

    print()

    length = int(input("Enter Your Length : "))

    width = int(input("Enter Your Width : "))

    print(f"The Answer Is : {length*width}")

  

  if ar == "4":

    print(str(undersc)*45)

    print()

    base = int(input("Enter Your Base : "))

    height = int(input("Enter Your Height : "))

    print(f"The Answer Is : {1/2*base*height}")

elif operation == "9":

    t = int(input("Which Table You Want : "))

    tw = int(input("Where Till You Want : "))

    print(str(undersc)*45)

    print()

    def table(num,till):

        till+=1

        for i in range(1,till):

            print(num*i)

    table(t,tw)

else:

    print("\ninvalid entry please try again !")



