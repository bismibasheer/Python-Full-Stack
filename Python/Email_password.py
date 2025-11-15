import re
pattern=r"[A-Z0-9a-z]+@[A-Z0-9a-z]+\.(in|com|dev)$"
Email=input("Enter your Email")
if re.match(pattern,Email):
    print("Valid User")
else:
    print("InValid User")  



import re
pattern1=r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\w).{8,}$"
password=input("Enter your Password")
if re.match(pattern1,password):
    print("Valid User")
else:
    print("InValid User") 
