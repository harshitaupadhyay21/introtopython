#*****question 1*****
#problem on tower of hanoi with three discs
print('******QUESTION-1:******')
#recursive function
def Towerofhanoi(n,from_rod,to_rod,aux_rod):
     if n==0:
         return
     Towerofhanoi(n-1,from_rod,aux_rod,to_rod)
     print('Move disk',n,'from rod',from_rod,'to rod',to_rod)
     Towerofhanoi(n-1,aux_rod,to_rod,from_rod)
n=3
Towerofhanoi(n,'A','B','C')
print('/n')
# A,B,C are the names of rods

#*****question 2*****
#problem to print pascal's triangle for n number of rows entered by the user using iteration
print('*******QUESTION-2*******')
n=int(input('Enter number of rows:'))

for i in range(1,n+1):
     for j in range(0,n-i+1):
          print(' ',end=' ')
     c=1
     for j in range(1,i+1):
          print(' ',c,sep=' ',end=' ')
          c=c*(i-j)//j
     print()
     print('/n')
#*****question 3*****
print('*******QUESTION-3:*******')
#Ask for user input of the two integers
int_1 = int(input("Enter first integer:"))
int_2 = int(input("Enter second integer:"))
print("")


#using divmod function print quotient and remainder
print("(Quotient, Remainder) is", divmod(int_1, int_2))
print("")


#converting divmod output to list; and printing the list
tuple_to_list = list(divmod(int_1, int_2)) 


#Part a
print("PART A Function is callable or not: ",callable(divmod(int_1, int_2)))
print("")


#Part b
print("PART B")
multiply = 1

#If multiply = 0 at the end, then zero is a part of the list. Otherwise, all elements are non-zero. 
for i in tuple_to_list:
    multiply = multiply*i
if multiply == 0:
    print("One/more digit is zero.")
else: 
    print("Since, multiplication of elements of a list is non-zero, None of the elements is zero.")
print("")


#Part c
print("PART C")
given_list = [4, 5, 6]
tuple_to_list.extend(given_list)
print("List after adding new values is", tuple_to_list)

#filtering values greater than 4
filtered_list = list(filter(lambda a : a<=4 ,tuple_to_list))
print("List after filtering out values greater than 4 is", filtered_list)
print("")


#Part d : convert list to set datatype
print("PART D: convert to set")
filtered_set = set(filtered_list)
print(filtered_set)
print("")


#part e: make set immutable
print("PART E: make set immutable")
immutable_set = frozenset(filtered_set)
print(immutable_set)
print("")


#part f : find max value of the set
print("PART D: find max value and find its hash")
max_value = max(immutable_set)
print("The maximum value from the set is ", max_value)
print("Hash value of the max value is ", hash(max_value))

print("-------------")



#******question-4*****
print('********QUESTION -4:*******')

class Student: #Creating class called Student
    def __init__(self, name, roll_number): 
        self.name = name 
        self.roll_number = roll_number 
        print("Student Class created.")

    def __del__(self): #Destroying the object
        print("Destructor called")

#Creating object
def create_object():
    print("Making an object...")
    obj = Student("Sample_Name", 123)
    print(f"The name of the student is {obj.name} and Roll Number is {obj.roll_number}")
    print("Function end...")
    return obj

#Calling create_object function
obj = create_object()
print("Program ended.")

#*****question-5*****

print('******QUESTION-5:******')
class Employee():
    def __init__(self, serial_number, name, salary):
        self.serial_number = serial_number
        self.name = name
        self.salary = salary
    def print_details(self):
        print(self.serial_number,self.name, self.salary )

#Entering employee information 
employee_1 = Employee(1, "Mehak", 40000)
employee_2 = Employee(2, "Ashok", 50000)
employee_3 = Employee(3, "Viren", 60000)


print("Details of Employees:")
employee_1.print_details()
employee_2.print_details()
employee_3.print_details()
print("------")
print("")

print("PART A")
# part a) modify Mehak's salary
employee_1.salary = 70000
employee_1.print_details()
print("")

print("PART B - refer to code as no output had to be printed for this part.")
#part b) delete Viren's record
del employee_3
#*****question-6*****

print('******QUESTION-6:******')

input_friend1 = str(input("Enter the word from friend 1:")).lower()
input_friend2 = str(input("Enter the word from friend 2:")).lower()

list_word = []

def split_dict(word):
    letters = []
    for x in word:
        letters.append(x)
    string_dict = {}
    for letter in letters:
        if letter in string_dict:
            string_dict[letter] += 1
        else:
            string_dict[letter] = 1
    global list_word
    list_word.append(string_dict)



split_dict(word = input_friend1)
split_dict(word = input_friend2)


#store each element of list_word to a separate variable
dict1 = list_word[0]
dict2 = list_word[1]

for i in dict1:
    if i in dict2: 
        #letter matched. 
        #now match the value
        if dict1[i] == dict2[i]:
            #value matched
            print(" :)")
            print("")
        else: 
            print(" :( ")
            print("")
    else: 
        print(" :( ")
        print("")

#ask shopkeeper for input to check result of for loop;and also check if the word is meaningful
print("")

shopkeeper1 = str(input("Press N if any of the above result was :( , otherwise press Y  ---- ")).lower()


print("")
print("")
if shopkeeper1 == 'y':
    shopkeeper = str(input("Does the word 2 make sense? Y/n ---- ")).lower()
    if shopkeeper == "y":
        print("Friendship is true")
        print("")
    else:
        print("Fake friendship! Don't worry, this is for fun!")
else: 
    print("Fake friendship! Don't worry, this is for fun!")





      


     
