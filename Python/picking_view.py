import pickle

with open("student_details.pkl","rb") as my_file:
   print(pickle.load(my_file))