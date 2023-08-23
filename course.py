# Gaza Sky Geeks | IT Foundation 8 Chohort - Class 3 Reem
# Final Project
# Course Class Module


class Course:
    course_id = 1
    course_levels = ["A", "B", "C"]
    def __init__(self, course_name, course_level):
        self.course_id = Course.course_id
        Course.course_id += 1
        self.course_name = course_name
        self.course_level = course_level.upper()


    def show_course_details(self): # Additional method to show courses for choose when 
                                   #we add course to student.
        print(f"\"{self.course_id}\" is the id of \"{self.course_name.capitalize()}\"" 
              f" course that available for \"{self.course_level}\" level.")


        