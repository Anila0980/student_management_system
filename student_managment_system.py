import json 

Students=[
   {
      "Name":"Anila",
      "Age":23,
      "Marks":90,
      "Grade":"A+"
   },
   {
      "Name":"Afra",
      "Age":19,
      "Marks":98,
      "Grade":"A+"

   },

   {
     "Name":"Ahmad",
      "Age":20,
      "Marks":89,
      "Grade":"A" 
   }]

def get_integer(message):#create a function using exception handling to handle enter incorrect input
 while True:
    try:
       varible=int(input(message))
       return varible
    except ValueError:
        print("Enter valid Number")  
             

def age_validate(age):
    if age<0 or age>45:
        return True
    return False
def validate_marks(marks):
      if marks< 0 or marks>100:
        
        return True
      return False
def save_data():#save data to json file
    with open("Students.json","w")as file:
        json.dump(Students,file)
def load_data():
    with open("Students.json","r")as file:
        return json.load(file)
def already_exit(name): 
    for student in Students:
        if student["Name"]==name:
             print("Students Already exit")
             return True
        return False
def add_student():#Create a function to add a student
    name=input("Enter Name")
    if already_exit(name):
        return
    age=get_integer("Enter Age")
    if age_validate(age):
        print("invalid Age")
    marks=get_integer("Enter Marks")
    while True:
        if validate_marks(marks):
            print("invalid marks")
            marks=int(input("Enter a valid marks"))
            
        else: 
            break   
    grade=input("Enter Grade")
    new_student={
          "Name":name,
          "Age":age,
          "Marks":marks,
          "Grade":grade
        
}    
    Students.append(new_student)
    save_data()
def view_student():#creat function to view student
    name=input("Enter Name:")
    for student in Students:
        if student["Name"]==name:
            print(student) 

def update_student():#creat function to update student
    name=input("Enter Name")
    for student in Students:
         if student["Name"]==name:
             new_age=int(input(" Enter new Age:"))
             if age_validate(new_age):
                print("invalid Age")
             new_marks=int(input("Enter New marks:"))
             while True:
                if validate_marks(new_marks):
                  print("invalid marks")
                  new_marks=int(input("Enter valid marks"))
                else:
                    break 
             new_grade=input("Enter new grade")
             student["Age"]=new_age
             student["Marks"]=new_marks
             student["Grade"]=new_grade
             print(student)
    save_data()           
def search_student():#create a function to search for a student
    name=input("Enter student Name")
    for student in Students:
        if student["Name"]==name:
             print(student)
def Delete_student():#create  a function to Delete a student
    name=input("Enter Name")
    for student in Students:
        if student["Name"]==name:
            Students.remove(student)
    save_data()       
def EXIT():
     print("Exit")
Students=load_data() #call the load to read data from the json file 
while True:    
    print("Enter choice to select menu:")
    print("1.Add student")
    print("2.View student")
    print("3.Update student")
    print("4.Search student")
    print("5.Delete student")
    print("6.Exit Menu")
    choice=get_integer(" Enter your Choice:")
    if choice==1:
        
        add_student()
    elif choice==2:
        view_student()    
    elif choice==3:
        update_student()
    elif choice==4:
        search_student()  
    elif choice==5:
        Delete_student()   
    elif choice==6:
        EXIT()
        break 
    else:
        print("Enter a valid Number")    
    