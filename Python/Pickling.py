import pickle
student={"name":"bismi","age":23,6:9}
with open("student_details.pkl","wb") as my_file:
   pickle.dump(student,my_file)

