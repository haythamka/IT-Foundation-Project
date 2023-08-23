# Gaza Sky Geeks | IT Foundation 8 Chohort - Class 3 Reem
# Final Project
# Students Functions Module


from course import Course
from course_functions import courses
from student import Student


students = [Student("haytham", "A"), Student("Fedaa", "B"), Student("Yaman", "C")]
# students = []
def add_new_student():
    name = input("Insert student name: ")
    print("")
    if name.replace(" ", "", len(name)).isalpha():
        valid_level = False
        while not valid_level: # Using While loop to ask user insert valid level.
            level = input("What is student leve? A|B|C: ")
            print("")
            if level.strip().upper() in Course.course_levels:
                students.append(Student(name, level))
                print("The student is added successfully.")
                print("")
                valid_level = True
            else:
                print(f"\"{level}\" is not a class level, try again.")
                print("")
    else:
        print("WARNING! Invalid name")
        print("")
        


def remove_student():
    number_valid = False
    while not number_valid:
        id_to_remove = input("Set the id of student to remove: ")
        print("")
        if id_to_remove.isdigit():
            remov_id = int(id_to_remove)
            for i in range(len(students)):
                if remov_id != students[i].student_id:
                    remov = False
                    continue
                else:
                    remov = True
                    students.remove(students[i])
                    print("Remove operation is done.")
                    print("")
                    break  
                
            if remov == False:
                print(f"The student with id:{remov_id} is not exist.")
                print("")
            number_valid = True           
        else:
            print("Please insert valid number.")
            print("")
            number_valid == False
        
    
        


def edit_student():
    if len(students) > 0:
        stud = input("Set the student id for edit: ")
        print("")

        if stud.isdigit():
            stud_id = int(stud)
            for i in range(len(students)):
                if students[i].student_id != stud_id:
                    edt = False
                    continue
                else:
                    edt = True
                    new_name = input("Write the new name of student: ")
                    print("")
                    if new_name.replace(" ", "", len(new_name)).isalpha():
                        new_level = input("Set new level of student, A|B|C: ")
                        print("")
                        if new_level.strip().upper() in Course.course_levels:
                            students[i].student_name = new_name
                            students[i].student_level = new_level
                            print("Edit operation is done.")
                            print("")
                            break
                        else:
                            print("Try to insert valid level (A|B|C).")
                            print("")
                            
                    else:
                        print(f"{new_name} is not a valid name, try with valid one.")
                        print("")
                        # edit_student()  
            if edt == False:
                print(f"The student with id:{stud_id} is not exist.")
                print("")
                # edit_student()
        else:
            print("Please insert valid number.")
            print("")
            # edit_student()
    else:
        print("The students list is empty.")
        print("")
        # edit_student()


def add_course_to_student():
    if len(courses) > 0:
        st_id = input("Insert the Student id to add course in his courses: ")
        print("")
        if st_id.isdigit():
            studnt_id = int(st_id)
            for i in range(0, len(students), 1):
                if studnt_id != students[i].student_id:
                    student_exist = False
                    continue
                else:
                    student_exist = True
                    corse_id = input(f"Insert the id of the course to add"
                                    f" it in \"{students[i].student_name}\" courses: ")
                    print("")
                    if corse_id.isdigit():
                        id = int(corse_id)
                        for j in range(len(courses)):
                            if id != courses[j].course_id:
                                course_exist = False
                                continue
                            else:
                                course_exist = True
                                students[i].add_new_course(courses[j])
                                break
                        if course_exist == False:
                            print(f"The course with id:\"{studnt_id}\" is not exist.")
                            print("")    
                            # add_course_to_student()
                        break
                    else:
                        print("Invalid id")
                        print("")
                        # add_course_to_student()
            if student_exist == False:
                print(f"The student with id:{studnt_id} is not exist.")
                print("")
                # add_course_to_student()
        else:
            print("Please insert valid number.")
            print("")
    else:
        print("The courses list is empty.")
        print("")
        # add_course_to_student()


def display_all_students():
    for student in students:
        student.show_student_data()
        print("*" * 15)

