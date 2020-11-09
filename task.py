# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

import school
import classes
import student

if __name__ == "__main__":
   kowalski = student.Student('Jan', 'Kowalski', [1,3,5,2,1,3,6,1], 7, 3)
   nowak = student.Student('Jakub', 'Nowak', [5,5,3,2,1], 12, 0)
   parek = student.Student('Staszek', 'Parek', [1,3,6,1], 3, 3)
   znuj = student.Student('Bartek', 'Znuj', [1,1,2,3,2,2], 2, 11)
   fer = student.Student('Mirek', 'Fer', [1,2,3,4,5,6,7,8], 10, 6)

   firstClass = classes.Classes('1A', [kowalski, nowak, parek])
   secondClass = classes.Classes('2A', [znuj, fer])

   highscool = school.School()
   highscool.addClass(firstClass)
   highscool.addClass(secondClass)

   print('Classes in school: ')
   highscool.printClasses()

   print('Students avg score across all classes: {}'.format(highscool.studetnsAvg()))

   print('Students avg score in class 2A: {}'.format(highscool.studetnsAvgInClass('2A')))

   print('Students in class 1A:')
   highscool.printClassStudents('1A')

   print('Scool average attendence: {}'.format(highscool.getSchoolAttendenceAvg()))