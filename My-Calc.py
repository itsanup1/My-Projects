def calc():
    import math as m
    spundersc = "_ "
    print(str(spundersc)*23)
    print()
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
        num1 = float(input("Enter Your 1st Num : "))
        num2 = float(input("Enter Your 2nd Num : "))
        print(f"The Ans Is : {num1 + num2}")
        calc()

    elif operation == "2":
        print(str(undersc)*45)
        print()
        num1 = float(input("Enter Your 1st Num : "))
        num2 = float(input("Enter Your 2nd Num : "))
        print(f"The Ans Is : {num1 - num2}")
        calc()

    elif operation == "3":
        print(str(undersc)*45)
        print()
        num1 = float(input("Enter Your 1st Num : "))
        num2 = float(input("Enter Your 2nd Num : "))
        print(f"The Answer Is : {num1 * num2}")
        calc()

    elif operation == "4":
        print(str(undersc)*45)
        print()
        num1 = float(input("Enter Your 1st Num : "))
        num2 = float(input("Enter Your 2nd Num : "))
        print(f"The Ans Is : {num1 / num2}")
        calc()

    elif operation == "5":
	      print(str(undersc)*45)	  
	      print()
	      num1 = float(input("Enter Your Num : "))
	      print(m.pow(num1,2))
	      calc()

    elif operation == "6":
  	    print(str(undersc)*45)
  	    print()
  	    num1 = float(input("Enter Your Num : "))
  	    print(m.sqrt(num1))
  	    calc()

    elif operation == "7":
        print(str(undersc)*45)
        print()
        print("1. Circle \n2. Square \n3. Rectangle \n4. Triangle")
        cir = input("Which Num Of Perimeter do you want to find : ")
        calc()

        if cir == "1":
             print(str(undersc)*45)
             print()
             r = float(input("\nEnter Radius of Circle : "))
             print(f"The Answer Is : {2*m.pi*r}") 
             calc()

        if cir == "2":
          print(str(undersc)*45)
          print()
          side = float(input("Enter Side of Square : "))
          print(f"The Answer Is : {side*4}")  
          calc()

        if cir == "3":
          print(str(undersc)*45)
          print()
          side1=float(input("Enter Length : "))
          side2=float(input("Enter Widgth : "))
          print(f"The Answer Is : {side1+side1+side2+side2}")
          calc()

        if cir == "4":
          print(str(undersc)*45)
          print()
          side1=float(input("Enter Length 1st Side : "))
          side2=float(input("Enter Length 2nd Side : "))
          side3=float(input("Enter Length 3rd Side : "))
          print(f"The Answer Is : {side1 + side2 +side3}")
          calc()

    elif operation == "8":
      print(str(undersc)*45)
      print()
      print("1. Circle \n2. Square \n3. Rectangle \n4. Triangle")
      ar = input("\nWhich No of Area You Want to Find : ")
      calc()

      if ar == "1":
        print(str(undersc)*45)
        print()
        r = float(input("Enter Radius : "))
        print(f"The Answer Is : {m.pi*m.pow(r,2)}") 
        calc()

      if ar == "2":
        print(str(undersc)*45)
        print()
        side = float(input("Enter The Side : "))
        print(f"The Answer Is : {m.pow(side,2)}")          
        calc()

      if ar == "3":
        print(str(undersc)*45)
        print()
        length = float(input("Enter Your Length : "))
        width = float(input("Enter Your Width : "))
        print(f"The Answer Is : {length*width}")  
        calc()

      if ar == "4":
         print(str(undersc)*45)
         print()
         base = float(input("Enter Your Base : "))
         height = float(input("Enter Your Height : "))
         print(f"The Answer Is : {1/2*base*height}")
         calc()

    elif operation == "9":
        t = float(input("Which Table You Want : "))
        tw = int(input("Where Till You Want : "))
        print(str(undersc)*45)
        print()
        

        def table(num,till):
             till+=1
             for i in range(1,till):
                 print(num*i)
        table(t,tw)
        calc()
    
    else:
        print("\ninvalid entry please try again !")    
        calc()
    
calc()
    
