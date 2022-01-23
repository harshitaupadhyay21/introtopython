#****ques1****
given='Python is a case sensitive language'
print(len(given))
print('the reversed string is'+given[::-1])
new_string=given[9:26]
print(new_string)
print(given.replace('a case sensitive','object oriented'))
print(given.index('a'))
print(given.strip())
print()
#****ques2****
name='Harshita Upadhyay'
sid=21104047
cgpa=9.9
dept='Electrical'
data='''Hey,{} here!
My SID is {}
I am from {} department and my CGPA is {}'''
print(data.format(name,sid,dept,cgpa))
print()
#****ques3****
a,b=56,10
print(a&b)
print(a|b)
print(a^b)
print(a<<2 and b<<2)
print(a>>2 and b>>4)
print()
#****ques4****
num1=int(input('Enter the 1st number:'))
num2=int(input('Enter the 2nd number:'))
num3=int(input('Enter the 3rd number:'))
if num1>num2 and num2>num3:
     largest=num1
elif num2>num3 and num3>num1:
     largest=num2
else:
     largest=num3
     print('the greatest number is:',largest)
print()
#****ques5****
abc=str(input('Enter something'))
if 'name' in abc:
    print('yes')
else:
    print('no')
print()
#****ques6****
s1=int(input('Enter 1st side:'))
s2=int(input('Enter 2nd side:'))
s3=int(input('Enter 3rd side:'))
if s1>s2+s3 or s2>s3+s1 or s3>s1+s2:
    print('No,the given sides cannot form a triangle')
else:
    print('Yes, the given sides can form a triangle')
print()

        
