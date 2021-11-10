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

    def rate_hw(self, lecturer, course, grade,student):
        if isinstance(lecturer, Mentor) and course in self.courses_in_progress and course in student.courses_in_progress_m:
            if course in lecturer.grades_M:
                lecturer.grades_M[course] += [grade]
            else:
                lecturer.grades_M[course] = [grade]
        else:
            return 'Ошибка'

    def mid(self, student, grades):
        for number in grades:
            all_num = number + number
            if best_student in Student:
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

        def __str__(self, mid, courses_in_progress, finished_courses):
            res = print(f' имя:{cool_mentor[0:1]}\n фамилия:{cool_mentor[1:2]}\n средняя оценка:{mid()}\n курсы в процессе изучения:{courses_in_progress}\n завершенные курсы:{finished_courses}')

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
            for number in grades_M:
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

            def __str__(self, mid_m):
                rel = print(f' имя:{cool_mentor[0:1]}\n фамилия:{cool_mentor[1:2]}\n средняя оценка:{mid_m()}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        def __str__(self):
            rer = print(f' имя:{cool_mentor[0:1]}\n фамилия:{cool_mentor[1:2]}')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

some_reviewer = str()

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
print(some_reviewer())