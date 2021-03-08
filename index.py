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
def hello(name):
    print("Hello " + name)
hello("Tshepo!")

#Task 0.4  function named even_or_odd 
def even_or_odd(num):
    if(num % 2 == 0):
        print("even")
    else:
        print("odd")


#Task 0.5 function of a triangle 
def triangle(s1, s2, s3): 
	s = (s1+s2+s3)/2
	return (s*(s - s1)*(s - s2)*(s - s3)) ** 0.5
print(triangle(20, 10 ,20))

#Task 0.6   Task 0.6 - good job. Now modify this fucntion to take any number of arguments.

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

def celsius_to_fahrenheit(temp):
    return ((temp * 9/5) + 32)
print(celsius_to_fahrenheit(14))

def fahrenheit_to_celsius(temp):
    return ((temp - 32) * (5/9))
print(fahrenheit_to_celsius(-17))

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
def common_letters(str1,str2):
    common = []
    for let1 in list(str1):
        for let2 in list(str2):
            if(let2==let1 and (let1 not in common)):
                common.append(let1)
    return ",".join(common)

if __name__ == '__main__':
	print(common_letters('house','computers'))


