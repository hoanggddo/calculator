print("Texas Instruments")
name=input("Name")
choose=False
print("1. Arithmetic")
print("2. Quadratic Equation Solver")
print("3. Greatest Common Denominator")
Choose=input("What number would you like? 1,2,3")
while choose==False:
  if Choose=="1":
     choose=True
     print("1. Addition")
     print("2. Subtraction")
     print("3. Multiplication")
     print("4. Division")
     print("5. Floor Division")
     print("6. Modulo")
     print("7. Exponentiation")
     choose1=input("What number would you choose?1-7")
     if choose1=="1":
      leftside1=int(input("left side number"))
      rightside1=int(input("right side number"))
      answer11=(leftside1 + rightside1)
      print(answer11)
     if choose1=="2":
       leftside1=int(input("left side number"))
       rightside1=int(input("right side number"))
       answer12=(leftside1 - rightside1)
       print(answer12)
     if choose1=="3":
       leftside1=int(input("left side number"))
       rightside1=int(input("right side number"))
       answer13=(leftside1 * rightside1)
       print(answer13)
     if choose1=="4":
       leftside1=int(input("left side number"))
       rightside1=int(input("right side number"))
       answer14=(leftside1 / rightside1)
       print(answer14)
     if choose1=="5":
       leftside1=int(input("left side number"))
       rightside1=int(input("right side number"))
       answer15=(leftside1 // rightside1)
       print(answer15)
     if choose1=="6":
       leftside1=int(input("left side number"))
       rightside1=int(input("right side number"))
       answer16=(leftside1 % rightside1)
       print(answer16)
     if choose1=="7":
       leftside1=int(input("left side number"))
       rightside1=int(input("right side number"))
       answer17=(leftside1 ** rightside1)
       print(answer17)
  if Choose=="2":
     choose=True
     a=int(input("1st term"))
     b=int(input("2nd term"))
     c=int(input("3rd term"))
     discriminant=(b**2-4*a*c)**1/2
     answer2=(-b-(discriminant))/(2*a)
     answer21=(-b+(discriminant))/(2*a)
     print(answer2, answer21)
  if Choose=="3":
     choose=True
     small=int(input("small number"))
     big=int(input("big number"))
     remandier=False
     while remandier==False:
        big, small=(small, big % small)
        if small==0:
          remandier=True
          print(big)

  else:
       print("1. Arithmetic")
       print("2. Quadratic Equation Solver")
       print("3. Greatest Common Denominator")
       Choose=input("What number would you like? 1,2,3")