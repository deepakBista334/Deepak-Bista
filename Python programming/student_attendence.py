def add_student():
    print("you are on add student function")
    #code to add a student
    
def update_student():
    print("you are on update student function")
    #code to update a student  
    
def delete_student():
    print("you are on delet student function")
    #code to delet a student 
    
def view_students():
    print("you are on veiw students function")
    #code to veiw students
    
def take_attendance():
    print("you are on take attendance function")
        # code to take attendance
        
def view_attendance():
    print("you are on veiw attendance function") 
         # code to veiw attendance
         
         
print("Enter 1: to add a student")
print("Enter 2 to update Student")
print("Enter 3 to delete a student")
print("Enter 4 to view students")
print("Enter 5 to take attendance")
print("Enter 6 to view attendance")
print("Enter 7 to exit")
    
while True:
        option = input("Enter Menue No:")
        if option == "1":
            add_student()
        elif option == "2":
            update_student()
        elif option == "3":
            delete_student()
        elif option == "4":
            view_students()
        elif option == "5":
            take_attendance()
        elif option == "6":
            view_attendance()
        elif option == "7":
          print("Exiting the program")
        else:
          print("Invalid option, please try again.")


        





            
        
            
            
