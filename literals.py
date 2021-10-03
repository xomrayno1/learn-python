
#import math
from math import pi


#Numeric Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal
#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

#String Literals

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

#complex
c = 1 + 2j
print(c)

str = '''Xin chao Đây là việt nam '''
print (str[0:5])

numbers = [5,4,2,7,1]
print(numbers)

sets1 = {4,5,27,8}
print(isinstance(sets1, type(sets1)))


userInfo = {
    "name" : "Nguyen Chi Tam",
    "age"  : "22",
    16 : 17
}
print(userInfo['name'], userInfo['age'], userInfo[16])

print(dict([[1,2],[3,4]]))

num_int = 100
num_float = 251.1
new_num =  num_int + num_float
print(type(new_num))

print(pi)

val = 17 % 4 
print(val)

suit = 0
suit = suit & 10

print(suit)



x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)