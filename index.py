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
name = 'Hello Tshepo'
print(name)

#Task 0.4  function named even_or_odd
def evenOrOdd(num):
    if(num % 2 == 0):
        print(num, " is Even")
    else:
        print(num, "is Odd")

evenOrOdd(26)
evenOrOdd(25)

#Task 0.5 function of a triangle
a = 3
b = 4
c = 6
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)

#Task 0.6
x = max(1,2,3)

print(x)

#Task 0.7
celsius = 35.7

fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))re

#Task 0.8 coverting minutes to hours
import datetime
def convert(n):
   return str(datetime.timedelta(minutes = n))
n = 71
print(convert(n))

#Task 0.9 print out vowels
v = "fat cat sat on the mat"
for i in v:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
    print(i)

#Task 0.10 common letters
string1=("house")
string2=("computers")
a=list(set(sstring1)&set(sstring2))
print("Common letters:")
for i in a:
    print(i)

        