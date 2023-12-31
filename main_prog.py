# Gaza Sky Geeks | IT Foundation 8 Chohort - Class 3 Reem
# Final Project
# Main Program Module


import course_functions, student_functions, student, course

def main_page():
    in_choices = True
    while in_choices:
        print("Select choice please \n1- Add New Student.\n2- Remove Student.\n"
            "3- Edit Student.\n4- Display All Students.\n5- Create New Course.\n"
            "6- Add Course To Student.\n0- Exit")
        print("")
        x = input("Enter Your Choice number: ")
        print("")
        if x == "1":
            student_functions.add_new_student()
            
        elif x == "2":
            if len(student_functions.students) > 0: # Check if students list is not empty.
                student_functions.remove_student()
            else:
                print("The students list is empty.")
                print("")

        elif x == "3":
            student_functions.edit_student()
            
        elif x == "4":
            if len(student_functions.students) > 0: # To ensure that the list of students is not empty.
                for i in range(len(student_functions.students)):
                    student_functions.students[i].show_student_data()
                    print("*" * 15)
            else:
                print("Students list is empty")
                print("")
            
        elif x == "5":
            course_functions.create_new_course()
            
        elif x == "6":
            if len(course_functions.courses) > 0:
                print("There are the available courses to choose from;")
                print("")
                for i in range(len(course_functions.courses)): # Show the courses to choose from.
                    course_functions.courses[i].show_course_details()
                print("")
                student_functions.add_course_to_student()
            else:
                print("The courses list is empty.")
                print("")
            
        
        elif x == "0":
            print("Thanks for use this program") # End Message
            in_choices = False
        else:
            print("Invalid input, Please insert one of choices.")
            print("")
       
        
    

main_page()