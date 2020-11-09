class Student:
   def __init__(self, name, surname, marks, attendence, absence):
      self.name = name
      self.surname = surname
      self.marks = marks
      self.attendence = attendence
      self.absence = absence
      self.totalHours = attendence + absence

   def getMarksAvg(self):
      return sum(self.marks)/len(self.marks)

   def getAttendenceAvg(self):
      return self.attendence / self.totalHours