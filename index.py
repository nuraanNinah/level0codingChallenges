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

#Task 0.6   

def maximum(a, b, c): 
    if (a >= b) and (a >= c): 
        largest = a 
  
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
          
    return largest 

a = 1
b = 2
c = 3
print(maximum(a, b, c)) 

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

#Task 0.10 common letters
def common_letters(string_one, string_two):
  common = ["common letters:"]
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  print(common)
  return common


common_letters("house", "computers")


