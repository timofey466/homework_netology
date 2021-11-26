class Student():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    best_student = ('Ruoy', 'Eman', 'your_gender')

    def rate_hw(self, lecturer, course, grade,student):
        if isinstance(lecturer, Mentor) and course in self.courses_in_progress and course in student.courses_in_progress_m:
            if course in lecturer.grades_M:
                lecturer.grades_M[course] += [grade]
            else:
                lecturer.grades_M[course] = [grade]
        else:
            return 'Ошибка'

    def mid(grades):
        for number in grades:
            all_num = number + number
            if isinstance(best_student , Student):
                num_x = len(grades)
                midl_num =  all_num % num_x
                print(midl_num)

    def midl_best(self,midl_num):
        for number in midl_num:
            best_ln = len(best_student)
            midd = 0
        while best_ln >= midd:
            midd + 1
        if midd + 1:
            all_midl = midl_num + midl_num
            print(all_midl)

    def __str__(name, sur, mid, courses_in_progress, finished_courses):
        res = []
        res.append(
            {"name:", name}
        )
        res.append(
            {"surname:", sur}
        )
        res.append(
            {"midl_number:", mid}
        )
        res.append(
            {'courses study now:', courses_in_progress}
        )
        res.append(
            {'finished_vourses:', finished_courses}
        )
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_M = {}
        self.finished_courses_m = []
        self.courses_in_progress_m = []


class Lecturer(Mentor):
        def mid_m(self, lecturer, grades_M):
            for number in int(grades_M):
                all_num = number + number
                if cool_mentor in Mentor:
                    num_x = len(grades_M)
                    midl_num =  all_num % num_x
                    print(midl_num)

        def midl_best(self,midl_num):
            for number in midl_num:
                best_ln = len(cool_mentor)
                midd = 0
            while best_ln >= midd:
                midd + 1
            if midd + 1:
                mentor_all_midl = midl_num + midl_num
                print(mentor_all_midl)



 #       def __str__(name_, sur, mid_m):
  #          rel = []
   #         rel.append(
    #            {'name:', name_}
     #       )
      #      rel.append(
       #         {'surname:', sur}
        #    )
         #   rel.append(
          #      {'midl_number:', mid_m}
           # )
            #return rel


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    cool_mentor = ('Some', 'Buddy')

#    def __str__(cool_mentor, cool_sur):
 #       rer = {
  #          "name:", str(cool_mentor),
   #         "surname:", str(cool_sur)
    #    }
#
 #       return rer

number = 1,2,3,4,5,6,7,8,9,10

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

#print(Student.__str__('Ruoy','Eman',123, 'python', 'HTML, CSS'))
