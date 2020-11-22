import json

def get_student_class_school(surname, schools):
   for x in schools:
      info = x.have_student(surname)
      if(x.have_student(surname)):
         return info

def find_school_students(schools, schoolName):
   for x in schools:
      if(x.name == schoolName):
         x.print_all_students()

class School:
   def __init__(self, schoolName):
      self.name = schoolName
      self.classes = {}

   def get_student_avg(self, studentSurname, className):
      return self.classes[className].students[studentSurname].get_marks_avg()

   def all_school_grades(self):
      grades = []
      for x in self.classes:
         for st in self.classes[x].students:
            grades += self.classes[x].students[st].marks

      return grades

   def have_student(self, surname):
      for x in self.classes:
         if surname in self.classes[x].students:
            return self.name, self.classes[x].className

      return False

   def add_class(self, classToAdd):
      self.classes[classToAdd.className]=classToAdd

   def print_classes(self):
      for x in self.classes:
         print(self.classes[x].className)

   def students_avg(self):
      avg = 0
      for x in self.classes:
         avg += self.classes[x].get_class_avg()
      
      return avg/len(self.classes)

   def students_avg_in_class(self, className): 
      return self.classes[className].get_class_avg()

   def print_class_students(self, className): 
      return self.classes[className].print_students()

   def print_all_students(self): 
      for x in self.classes:
         print(self.classes[x].print_students())

   def get_school_attendence_avg(self):
      avg = 0
      for x in self.classes:
         avg += self.classes[x].get_class_attendence()
      
      return avg/len(self.classes)

class Classes:
   def __init__(self, className, students):
      self.className = className
      self.students = {}

   def get_class_avg(self):
      avg = 0
      for x in self.students:
         avg += self.students[x].get_marks_avg()

      return avg/len(self.students)

   def print_students(self):
      for x in self.students:
         print(self.students[x].name, self.students[x].surname)

   def get_class_attendence(self):
      avg = 0
      for x in self.students:
         avg += self.students[x].get_attendence_avg()

      return avg/len(self.students)

class Student:
   def __init__(self, name, surname, marks, attendence, absence):
      self.name = name
      self.surname = surname
      self.marks = marks
      self.attendence = attendence
      self.absence = absence
      self.totalHours = attendence + absence

   def get_marks_avg(self):
      return sum(self.marks)/len(self.marks)

   def get_attendence_avg(self):
      return self.attendence / self.totalHours

def read_file():
   data = json.load(open("data.json"))

   schools = []

   for schoolName, classes in data.items():
      newSchool = School(schoolName)

      for className, students in classes.items():
         newClass = Classes(className, [])

         for student in students:
            newStudent = Student(student['name'], student['surname'], student['grades'], student['attendence'], student['absence'])
            newClass.students[newStudent.surname] = newStudent

         newSchool.add_class(newClass)

      schools.append(newSchool)

   return schools


if __name__ == "__main__":
   schools = read_file()
   
   for x in schools:
      print(x.name)
      print('School grades avg: {}'.format(x.students_avg()))
      print('School attendence avg: {}'.format(x.get_school_attendence_avg()))
      print('School second class grades avg: {}'.format(x.students_avg_in_class('2')))
      print('All grades in school: {}'.format(x.all_school_grades()))
      print('\n')

   print('Parek avg grades: {}'.format(schools[0].get_student_avg("Parek", "2")))

   school, className = get_student_class_school("Kowal", schools)

   print('Kowal is in school {} and class {}'.format(school, className))

   print('Students in SchoolB')
   find_school_students(schools, 'SchoolB')
   