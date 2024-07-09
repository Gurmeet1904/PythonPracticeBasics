class Student:
    school = "ABC School"    #class variable

    def __init__(self, m1, m2, m3):    #m1, m2, m3 are instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):    # normal method
        return (self.m1 + self.m2 + self.m3)/3

    #class method is used when we are using class variables

    @classmethod                 #decorators
    def getSchoolName(cls):      #cls is used to access class variables
        return cls.school

    #static method is used when neither class variable nor instance variable is required

    @staticmethod
    def info():                 #This method takes neither instance variables nor class variable, hence it is called static method
        print("This is student class ... in ABC School")




s1 = Student(34, 56, 76)
s2 = Student(56,23,89)

print("Average of student 1 is ", s1.avg())
print("Average of student 2 is ", s2.avg())

print(Student.getSchoolName())
Student.info()
