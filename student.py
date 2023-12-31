# Gaza Sky Geeks | IT Foundation 8 Chohort - Class 3 Reem
# Final Project
# Student Class Module


from course import Course
# from Course_functions import courses

class Student:
    student_id = 1
    student_levels = ["A", "B", "C"]
    def __init__(self, student_name, student_level):
        self.student_id = Student.student_id
        Student.student_id += 1
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = []
# Method to add new course to student
# NOTE: I am using the course object instead of 
# course id as a parameter for this method, which will 
# come from another function after check operations, 
# to avoid using loops and long check operations inside 
# this method.


    def add_new_course(self, cours):  
        if (cours.course_level).lower() == (self.student_level).lower(): 
            self.student_courses.append(cours)
            print("Course is added successfully")
            print("")
        else:
            print(f"The course level is \"{cours.course_level}\", "
                  f"and is not available to \"{self.student_name}\" in \"{self.student_level}\" level")
            print("")
      

    def show_student_data(self):
        print(f"\"{self.student_name.capitalize()}\" is a student in the "
              f"\"{self.student_level}\" level with id \"{self.student_id}\".") 
        # The code below is To Show student courses (if exist)after basic student data
        # or show message to tell the user that no courses registered for this student.
        if len(self.student_courses) > 0:
            print("and these are the courses he is enrolled in:")
            print("")
            for course in self.student_courses:
                indx = (self.student_courses).index(course)
                print(f"{indx+1}- \"{course.course_name}\"")
        else:
            print("This student is not registered in any course") 
            print("")
















