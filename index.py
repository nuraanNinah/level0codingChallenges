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

#Task 0.7    

def fahrenheit_to_celsius(temp):
    return ((temp - 32) * (5/9))
print(fahrenheit_to_celsius(0))

def celsius_to_fahrenheit(temp):
    return ((temp * 9/5) + 32)
print(celsius_to_fahrenheit(0))


#Task 0.8 coverting minutes to hours
import datetime
def convert(n):
   return str(datetime.timedelta(minutes = n))
n = 71
print(convert(n))

#Task 0.9 print out vowels  
def vowels(text):
    vowels = "aeiouAEIOU"
    print([letter for letter in text if letter in vowels])
vowels('The fat cat sat on the mat')

#Task 0.10 common letters   Task 0.10 - missing a function.
string1=("house")
string2=("computers")
a=list(set(sstring1)&set(sstring2))
print("Common letters:")
for i in a:
    print(i)

        