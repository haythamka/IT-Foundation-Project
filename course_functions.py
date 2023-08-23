# Gaza Sky Geeks | IT Foundation 8 Chohort - Class 3 Reem
# Final Project
# Courses Functions Module

from course import Course


# courses = [Course("Math", "A"), Course("English", "B"), Course("Programming", "C")]
courses = []
#Function to create new course object and add it to courses list
def create_new_course():
    name = input("Insert Course title: ")
    print("")
    for course in courses:
        if name.lower() == (course.course_name).lower(): #Check if the course is already exist in courses list.
            print("This course is exist")
            print("")
            create_new_course()

    level = input("What is course leve? A|B|C: ") 
    if level.strip().upper() in Course.course_levels: # Check if the inserted level is one of levels (A,B,C) 
        courses.append(Course(name, level))
        print("The course is added successfully")
        print("")
    else:
        print(f"\"{level}\" is not a class level, try again.")
        print("")
        create_new_course()
    


