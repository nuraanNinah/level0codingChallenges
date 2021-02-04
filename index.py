#Task 0.1 
x = 0
y = 1
print(x)
print(y)


x = x + 3
y = y + x
print(x)
print(y

#Task 0.2
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + ( 1 * 2 )
a = 1 + 1 * 2 / 2
b = (1 + 1 * 2 ) /  2

print(x)
print(y)
print(z)
print(a)
print(b)

#Task 0.3 function named hello
def hello():
    print("Hello Tshepo!")
hello()

#Task 0.4  function named even_or_odd
def evenOrOdd(num):
    if(num % 2 == 0):
        print(num, " is Even")
    else:
        print(num, "is Odd")


#Task 0.5 function of a triangle 
def Triangle(s1, s2, s3):
	area = (2 * 3 * 2)/2
	return area

#Task 0.6   Task 0.6 - it is completely wrong. You are required to CREATE A FUNCTION that takes in 3 numbers (which you will have to modify to accommodate any set of numbers) and returns the biggest number out of them.
def maximum()
x = max(1,2,3)

print(x)

#Task 0.7    Task 0.7 - write two functions, to convert Fahrenheit to Celsius and another on to convert Celsius to Fahrenheit.
celsius = 35.7

fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))re

#Task 0.8 coverting minutes to hours
import datetime
def convert(n):
   return str(datetime.timedelta(minutes = n))
n = 71
print(convert(n))

#Task 0.9 print out vowels   Task 0.9 - missing a function 
v = "fat cat sat on the mat"
for i in v:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
    print(i)

#Task 0.10 common letters   Task 0.10 - missing a function.
string1=("house")
string2=("computers")
a=list(set(sstring1)&set(sstring2))
print("Common letters:")
for i in a:
    print(i)

        