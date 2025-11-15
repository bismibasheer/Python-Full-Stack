"""my_file=open("Sample_file.txt","w")
my_file.write("Hello Developers")
my_file.close()"""




"""with open("sample.txt","w") as my_file:
    my_file.write("python is a High level language")

with open("sample.txt","r") as my_file:
   content=my_file.read()
   print(content)"""



with open("image.jpg","rb") as my_file:
   content=my_file.read()

with open("newimage.jpg","wb") as my_file:
   my_file.write(content)
   

