class Classes:
   def __init__(self, className, students):
      self.className = className
      self.students = students

   def getClassAvg(self):
      avg = 0
      for x in self.students:
         avg += x.getMarksAvg()

      return avg/len(self.students)

   def printStudents(self):
      for x in self.students:
         print(x.name, x.surname)

   def getClassAttendence(self):
      avg = 0
      for x in self.students:
         avg += x.getAttendenceAvg()

      return avg/len(self.students)