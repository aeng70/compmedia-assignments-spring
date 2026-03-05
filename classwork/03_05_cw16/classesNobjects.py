#CODE ALONG: Create a minion class with several attributes - some that are the same 
#for every minion, and some that are different. 
#Create an instance of the class (an object!) and print it to the console.
#The above is the work we did in class, just copy paste it for reference.





#If time permits, continue adding attributes after the whole class portion is done.
#Otherwise, remember you must at least finish the mild task below.


#YOUR TASK: Complete the following to the best of your ability. Thank you to
#			Ms. Shuman for her example tasks!
#MILD 🌶

#1. Create a class called Student that has two attributes: a name, and a grade.

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Now create instances of three different students (student1, student2, and student3).

student1 = Student("archie", 11)
student2 = Student("stas", 11)
student3 = Student("ethan", 11)

#Confirm that the class works by printing out the first student's name.

print(student1.name)


# MEDIUM 🌶🌶

#2. Create a class called School that has three attributes: a name, a type, and
#	a size (number of students).

class School:
    def __init__(self, name, schoolType, schoolSize):
        self.name = name
        self.schoolType = schoolType
        self.schoolSize = schoolSize

#Create instances of three individual schools.

ps144 = School("P.S. 144", "Elementary", 805)
sage = School("Russell Sage", "Middle", 926)
stuy = School("Stuyvesant", "High", 3334)

#Confirm that the class works by printing out the name and size of the third school.

print(stuy.name, stuy.schoolSize)

###
#3. Create a class called House that has four attributes: an address, a number
#	of bathrooms, a price, and a number of bedrooms.

class House:
    def __init__(self, address, numBathrooms, price, numBedrooms):
        self.address = address
        self.numBathrooms = numBathrooms
        self.price = price
        self.numBedrooms = numBedrooms

#Create instances of at least three individual houses.

house = House("6 J St", 3, 1000000, 3)
apt = House("34 M St", 1, 400000, 1)
ch = House("9 E St", 2, 700000, 2)

#Confirm that the class works by printing out the address and size of the second house.



#SPICY 🌶🌶🌶

#4. Put your three students in a list called my_students, your houses in a list
#	for houses, and your schools in a list for schools.



#Iterate (this means use a loop!) over the student list, printing out "_____ is in
#grade __." For each of the students.



#Iterate over the houses list and print out a description for each one. Do the same
#for your schools lists.



###
#5. Modify your student class above to include a savings_account value for each
#	student. Change your initializers so that the code still runs. 



#Write some code that compares a student and a house, and determines whether or not
#the student can afford to buy the house. 