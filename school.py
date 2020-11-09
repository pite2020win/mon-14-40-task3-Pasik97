class School:
   def __init__(self):
      self.classes = {}

   def addClass(self, classToAdd):
      self.classes[classToAdd.className]=classToAdd

   def printClasses(self):
      for x in self.classes:
         print(self.classes[x].className)

   def studetnsAvg(self):
      avg = 0
      for x in self.classes:
         avg += self.classes[x].getClassAvg()
      
      return avg/len(self.classes)

   def studetnsAvgInClass(self, className): 
      return self.classes[className].getClassAvg()

   def printClassStudents(self, className): 
      return self.classes[className].printStudents()

   def getSchoolAttendenceAvg(self):
      avg = 0
      for x in self.classes:
         avg += self.classes[x].getClassAttendence()
      
      return avg/len(self.classes)

      