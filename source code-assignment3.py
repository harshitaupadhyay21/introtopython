#QUESTION 1
#Program to count the number of occurences of each word or character in the input string
print('question 1')

str=input('Enter a string')
chr=input('Enter a character:')
i=0
count=0

while (i<len(str)):
      if (str[i]==chr):
         count=count+1
      i+=1

print('The total number of times', chr ,'has occured=',count)

print('\n')
print('*' *160)




#QUESTION 2
# Program to display next date of input date.

print('question 2')

#take the input year from user and check if its a leap year.
year=int(input('Enter some year from 1800 to 2025'))
for year in range(1800,2025):

 if(year % 400==0):
   leap_year=True
 elif(year%100==0):
    leap_year=False
 elif(year%4==0):
    leap_year=True
 else:
    leap_year=False


#take the input month and check how many days does it have.
month=int(input('Enter a month[1-12]:'))

if month in (1,3,5,7,8,10,12):
    month_len=31
elif month==2:
     if leap_year:
         month_len=29
     else:
         month_len=28
else:
    month_len=30

#take the input day.
    day=int(input('input a day[1-31]:'))

    if day<month_len:
        day+=1
    else:
        day=1
        if month==12:
          month=1
          year+=1
        else:
          month+=1
#print the next day from the data entered by the user.

print('the next date is [YYYY/MM/DD]%d-%d-%d.'%(year,month,day))

print('\n')
print('*'*160)


#QUESTION-3
#Program to a list of tuples from a given list having number and its square in each tuple

print('question 4')
#create a list
list_1=[2,5,4,8]

#using list comprehension to iterate ecah value in list and create a tuple
result=[(x,x**2)for x in list_1]

print(result)

print('\n')
print('*'*160)

#QUESTION-4
#program to print grade and performance according to the grade points input by the user

print('question-4')

#make a dictionary to store students' details.
dict={4:'poor',5:'Below average',6:'Average',7:'good',8:'very good',9:'excellent',10:'outstanding'}
n=int(input('Input your grade:'))

if(n<4):
    print('Error')
else:
    print('Your grade is',end='')
    print(n)
    print(' and ',end='')
    print(dict.get(n),end='Performance')

print('\n')
print('*'*160)


#Question-5
#Program to print triangular pattern of alphabets.

print('Question-5')

i=0
pattern='ABCDEFGHIJK'

#Iterations to print the pattern.
for i in range(6):
    j=i
    while(j>0):
        print('',end='')
        j-=1
    k=0
    for k in range(len(pattern)-2*i):
        print(pattern[k],end='')
    print('')

print('\n')
print('*'*160)

#Question-6
#Program to perform operations on dictionary used to store students' details.

print('Question-6')
sid=int(input('Enter your SID:\n'))
name=input('Enter your name:')
students={sid:name}

while True:
    option=input('do you want to enter another student entry(y or n):')
    if option=='y':
        sid=int(input('Enter sid:'))
        name=input('Enter name:')
        students[sid]=name
    elif option=='n':
        break
    else:
        print('Invalid input!!')

#PART-a
#To print the dictionary.
print('<a>\n',students)

#Part-b
#to sort the students' details according to their names

print('<b>\n',{k:v for k,v in sorted(students.items(),key=lambda x:x[1])})

#Part-c
#sorting according to their sids:

print('<c\n>',{k:v for k,v in sorted(students.items())})

#part-d
#to search for a student by their sid

sid=int(input('Search name with SID for:\n'))
print('<d>\n',students[sid])

print('\n')
print('*'*160)

#Question-7
#Program to print the fibonacci series and print the average of resultant series.

print('question-7')
#to print fibonacci series entered by the user.

def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
nterms=int(input('Enter a positive integer for the number of terms of fibonacci series:'))

#check if the number of terms is valid.
if nterms<=0:
    print('Enter a positive integer')
else:
    print('Fibonacci sequence:')
    sum=0
    for i in range(nterms):
        print(recur_fibo(i))
        sum=sum+recur_fibo(i)
avg=float(sum/nterms)
print('Average of resultant fibonacci series is:',avg)


print('\n')
print('*'*160)

#Question-8
#program to perform operations on given set of numbers.

print('question-8')

s1={1,2,3,4,5}
s2={2,4,6,8}
s3={1,5,9,13,17}

#Part-a
print('part-a')

Set_union=s1.union(s2)
Set_intersection=s1.intersection(s2)
a=Set_union-Set_intersection
print('<a>\n',a)

#part-b
print('part-b')

b=s1.union(s2.union(s3))-s1.intersection(s2)-s2.intersection(s3)-s3.intersection(s1)
print('<b>\n',b)

#part-c
c=((s1.intersection(s2)).union((s1.intersection(s3)).union(s2.intersection(s3))))-s1.intersection(s2.intersection(s3))
print('<c>\n',c)

#part-d

d=set()
for i in range(1,11):
    if i not in s1:
        d.add(i)
    print('<d>\n',d)

#part-e

e=set()
if i in range(1,11):
    if i not in s1 and i not in s2 and i not in s3:
        e.add(i)
print('<e>\n',e)


