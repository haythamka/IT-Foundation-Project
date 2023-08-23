# Gaza Sky Geeks | IT Foundation 8 Chohort - Class 3 Reem
# Final Project
# Courses Functions Module

from course import Course


courses = [Course("Math", "A"), Course("English", "B"), Course("Programming", "C")]
# courses = []
#Function to create new course object and add it to courses list
def create_new_course():
    name = input("Insert Course title: ")
    print("")
    name_exist = False 
    for course in courses:
        if name.lower() == (course.course_name).lower(): #Check if the course is already 
            name_exist = True                                             #exist in courses list.
            
    if not name_exist: # If the inserted course name is not one of list courses then ask
                       # the user to insert the course leve.     
        level_valid = False
        while not level_valid: # Using While loop to ask user insert valid level when he insert invalid one.
            level = input("What is course leve? A|B|C: ") 
            if level.strip().upper() in Course.course_levels: # Check if the inserted 
                                                              #level is one of levels (A,B,C) 
                courses.append(Course(name, level))
                print("The course is added successfully")
                print("")
                level_valid = True
            else:
                print(f"\"{level}\" is not a class level, try again.")
                print("")
    else:
        print("This course is already exist")
        print("")
        
          


