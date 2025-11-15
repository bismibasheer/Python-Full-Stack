while True:  
       a=int(input("Enter your First Number"))
       b=int(input("Enter your Second Number"))
       print("Choose your Option /n 1.Add /n 2.Subtraction /n 3. Multiplication /n 4. Division")
       value=int(input("choose your option"))
       
       

       if value==1:
              print("Answer is",a+b)  
       elif value==2:
              print("Answer is",a-b) 
       elif value==3:
              print ("Answer is",a*b)
       else:
              print("Answer is",a/b)
       


       yes=input("Do you Want to continue (yes/No)")
       if yes=="No":
              break

  
