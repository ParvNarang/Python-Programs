while True:
   num = input(" ENTER THE NUMBER - ")
   print("*************This is the Menu *************")
   print("*************Here is a list of - 1)PRIME")
   print("                                 2)ARMSTRONG")
   print("                                 3)AUTOMORPHIC")
   print("                                 4)SPECIAL")
   print("                                 5)EXIT   ")
         
   j = input(" What you want to check that your number is. ")
   if j == "prime number" or j == "PrimeNumber" or j ==" primenumber" or j =="prime" or j=="1":
      print("     MENU FOR PRIME NUMBERS   ")
      num=int(num)
      #num = int(input(" Enter the number "))
      f=0
      for i in range(2,num):
         if x%i==0:
            f=1
      if f==0:
         print("     Prime Number")
      else:
         print("     Not Prime")

   elif j =="armstrongnumber" or j == "ArmStrong" or j=="arm strong" or j=="2":
      print("        MENU FOR ARMSTRONG      ")
      num=int(num)
      #num = int(input("Enter the number: ")) 
      sum = 0 
      y = num
      
      while (y > 0):
         x = y % 10 
         sum = sum + x ** 3
         y = y//10 
      if (num == sum):
         
         print("Armstrong number")
            
      else:
         print("Not an Armstrong number")

   elif j == "automorphic" or j =="Automorphic" or j=="3":
      print("         MENU FOR AUTOMORPHIC      ")
      #num = input("ENTER THE NUMBER")
      d=0
      l=0
      s=0
      l=len(num)
      num = int(num)
      s = num**2
      d = s%10**l
      if d == num:
         print("AUTO")
      else:
         print("NOT")

   elif j =="special" or j=="4":
      num = int(num)
      y=num
      t=0
      while True:
         if num>0:
            q = num%10
            s = 1
            for i in range(q,0,-1):
               s=s*i
            t=t+s
            num=num//10
         else:
            break
      if t==y:
         print("\tSpecial")

      else:
         print("\tNot Special")

   else:
      break
