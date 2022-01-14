#***answer1***
x=int(input('enter the 1st number: '))
y=int(input('enter the 2nd number: '))
z=int(input('enter the 3rd number: '))
avg=(x+y+z)/3
print('the average of numbers is : ', avg)

print()
print()

#***answer2***
income=int(input('enter your gross income: '))
dependent=int(input('enter number of dependents: '))
tax=income-10000-(dependent*3000)
print('your annual tax is:', tax*0.2)

print()
print()

#***answer3***
name=input('enter your name: ')
sid=int(input('enter your sid: '))
gender=input('enter your gender: ')
course=input('enter your course name: ')
cgpa=float(input('enter your cgpa: '))
student=[sid,name,gender,course,cgpa]
print(student)

print()
print()

#***answer4***
stu1=int(input('enter marks of 1st student:'))
stu2=int(input('enter marks of 2nd student:'))
stu3=int(input('enter marks of 3rd student:'))
stu4=int(input('enter marks of 4th student:'))
stu5=int(input('enter marks of 5th student:'))
marks=[stu1,stu2,stu3,stu4,stu5]
marks.sort()
print(marks)

print()
print()

#***answer5***
color=['Red','Green','White','black','pink','yellow']
print(color)
#***part a***
del color[3]
print('after deleting the 4th item ,new list is;',color)
#***part b***
color=['Red','Green','White','black','pink','yellow']
color[3]=color[4]='purple'
print('answer for part b is:',color[0:4]+color[5:])

