# Gaza Sky Geeks | IT Foundation 8 Chohort - Class 3 Reem
# Final Project
# Main Program Module


import course_functions, student_functions, student, course

def main_page():
    print("Select choice please \n1- Add New Student.\n2- Remove Student.\n"
          "3- Edit Student.\n4- Display All Students.\n5- Create New Course.\n"
          "6- Add Course To Student.\n0- Exit")
    print("")
    x = input("Enter Your Choice number: ")
    print("")
    if x == "1":
        student_functions.add_new_student()
        main_page()
    elif x == "2":
        student_functions.remove_student()
        main_page()
    elif x == "3":
        student_functions.edit_student()
        main_page()
    elif x == "4":
        if len(student_functions.students) > 0:
            for i in range(len(student_functions.students)):
                student_functions.students[i].show_student_data()
                print("*" * 15)
        else:
            print("Students list is empty")
            print("")
        main_page()
    elif x == "5":
        course_functions.create_new_course()
        main_page()
    elif x == "6":
        print("There are the available courses to choose from;")
        print("")
        for i in range(len(course_functions.courses)): # Show the courses to choose from.
            course_functions.courses[i].show_course_details()
        print("")
        student_functions.add_course_to_student()
        main_page()
    elif x == "0":
        print("Thanks for use this program")
    else:
        print("WARNING! Please insert one of choices.")
        print("")
        main_page()
        
    

main_page()