'''
Department codes:
"A" = Geography department
"B" = History department
"C" = Mathematics department
"D" = Physics department
Subject codes:
"Geography = GEO"
"Geology = GLA"
"Oceanography" = "OCN"
"Climatology" = "CLM"
"History" = "HIS"
"Anthropology" = "ANP"
"Mathematics" = "MATH"
"Physics" = "PHY"
'''
class Person: #creating a class Person
  def __init__(self, name, address, ph, email):
    self.name = name
    self.address = address
    self.ph = ph
    self.email = email
  def getDetails(self): #method to get all details about Person
    print (f"Name: {self.name}\nAddress: {self.address}\nPhone number: {self.ph}\nEmail: {self.email}")
class Course: #a new class named Course created
  Courses = [] #all the object Course will append here
  spec = {} #the subject code and the subject respectedly will be added as dictionary
  Max_capacity = {}
  def __init__(self, course_code, course_name, maximum_capacity = 0):
    self.c_code = course_code
    self.c_name = course_name
    self.max_cap = maximum_capacity
    Course.Courses.append(course_name)
    Course.Max_capacity[course_name] = maximum_capacity
    Course.spec[course_code]= course_name #The subject code and the subject will be added to spec for further use
  def CourseDetails(self): #function to get Course details
    enrolled_Students = Student.course_based_count.get(self.c_name.lower(), 0) #To count the number of student enrolled for the particular subject
    print (f"Course name: {self.c_name}\nCourse code: {self.c_code}\nMaximum capacity: {self.max_cap}\nEnrolled Student: {enrolled_Students}")
class Student(Person): #creating Student class
  status = "Active"
  count = 0 #couunt for Student
  course_based_count = {'geography':0,'geology':0,'oceanography':0,'climatology':0,'history':0,'anthropology':0,'mathematics':0,'physics':0}#COunt of student in every sub
  def __init__(self,name, address, ph, email, course_enrolled):
    super().__init__(name, address, ph, email) #info going to super class(person)
    Student.count += 1
    self.en = course_enrolled
    self.ID = ('STID')+(str(Student.count)) #making Student ID
    # for e in Student.course_based_count:
    #   if course_enrolled.lower() in e:
    #     Student.course_based_count[e] += 1 # +1 will be added for the particular subject
    if Course.Max_capacity[self.en.capitalize()] <= Student.course_based_count[self.en.lower()]:
      print(f"Cannot enroll {self.name} in {course_enrolled}. Maximum capacity reached.")
      self.status = "Not Enrolled"
    else:
        Student.course_based_count[course_enrolled.lower()] += 1
        self.status = "Active"
        print ("The student is enrolled.")
  def StudentDetails(self): #method to get details about Student
    print (f"Student Name: {self.name}\nAddress: {self.address}\nPhone number: {self.ph}\nEmail: {self.email}\nStudent ID: {self.ID}\nCourse enrolled: {self.en}\nStatus: {Student.status}")
class Professor(Person):
  proCodeA = [] #Professor code A contains all the Professors who are enlisted for Geography Department
  proCodeB = [] #Professor code B contains all the Professors who are enlisted for History Department
  proCodeC = [] #Professor code C contains all the Professors who are enlisted for Mathematics Department
  proCodeD = [] #Professor code D contains all the Professors who are enlisted for Physics Department
  status = "Active"
  count = 0 #count for Professor
  def __init__(self, name, address, ph, email, course_spec, interns=0):
    super().__init__(name, address, ph, email)
    Professor.count += 1 #count added for professor when creating a class
    self.Course = course_spec
    self.interns = interns
    for i in course_spec: #creating list for every department code wise
      if i[-1] == 'A' and name not in Professor.proCodeA:
        Professor.proCodeA.append(name)
      elif i[-1] == 'B' and name not in Professor.proCodeB:
        Professor.proCodeB.append(name)
      elif i[-1] == 'C' and name not in Professor.proCodeC:
        Professor.proCodeC.append(name)
      elif i[-1] == 'D' and name not in Professor.proCodeD:
        Professor.proCodeD.append(name)
    self.ID = ('PRID')+(str(Professor.count)) #making Professor ID
  def profDetails(self):
    print (f"Name: {self.name}\nAddress: {self.address}\nPhone number: {self.ph}\nEmail: {self.email}\nEmployee ID: {self.ID}\nCourse specification: {self.Course}\nStatus: {Professor.status}\nInterns: {self.interns}")

class Department(Course): #Department class created
  departments = [] #all the object will add here
  codeCourseA = [] #code A for Geography
  codeCourseB = [] #code B for History
  codeCourseC = [] #code C for Math
  codeCourseD = [] #code D for Physics
  def __init__(self, department_code, department_name):
    self.dept_code = department_code
    self.dept_name = department_name
    Department.departments.append(department_name) #departments will be added to departments attribute
    if department_name.lower() == 'geography':
      self.prof = Professor.proCodeA
    elif department_name.lower() == 'history':
      self.prof = Professor.proCodeB
    elif department_name.lower() == 'mathematics':
      self.prof = Professor.proCodeC
    elif department_name.lower() == 'physics':
      self.prof = Professor.proCodeD
    for key, value in Course.spec.items(): #Department wise the courses will be added
      if key[-1] == 'A' and value not in Department.codeCourseA:
        Department.codeCourseA.append(value)
      elif key[-1] == 'B' and value not in Department.codeCourseB:
        Department.codeCourseB.append(value)
      elif key[-1] == 'C' and value not in Department.codeCourseC:
        Department.codeCourseC.append(value)
      elif key[-1] == 'D' and value not in Department.codeCourseD:
        Department.codeCourseD.append(value)
  def DepartmentDetails(self): #All the courses offered by the respected department will be added using self.subs
    if self.dept_name.lower() == 'geography':
      self.subs = Department.codeCourseA
    elif self.dept_name.lower() == 'history':
      self.subs = Department.codeCourseB
    elif self.dept_name.lower() == 'mathematics':
      self.subs = Department.codeCourseC
    elif self.dept_name.lower() == 'physics':
      self.subs = Department.codeCourseD
    print (f"Department name: {self.dept_name}\nDepartment code: {self.dept_code}\nCourse offered: {self.subs}\nProfessors: {self.prof}")
    
