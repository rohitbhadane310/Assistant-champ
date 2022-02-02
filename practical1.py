# ---------------> 1A) Explore Comments, Numeric data types and String data types

# -----> Explore Comments

# This is a singe line comment
print("A.c patil college ")

#This is a comment
#written in
#more than just one line
print("Hello Rohit ")


"""
This is a comment  written in
more than just one line
"""
print("students ")


# ------> Explore varible and Numeric data types

# 1) Explore different tyes of varible
num1 = 3
num2 = 6.8
v = "Rohit"

print("The value of num1 is => ", num1)
print("The value of num2 is => ", num2)
print("The V is ", v)

# 2) Typecasting
x=56
y=3.4
z="Rohit"
print("The data type x is ",type(x))
print("The data type y is ",type(y))
print("The data type z is ",type(z))


# ------> Numeric data types

val1 = 54   
val2 = 4.5  
cn = 5+3j  

print("The type of val1 is ", type(val1))  
print("The type of val2 is ", type(val2))  
print("The type of cn is ", type(cn))  
print("cn is a complex number", isinstance(5+3j,complex))
print("val1 is a interger number", isinstance(54,int)) 
print("val2 is a interger number", isinstance(4.5,int)) 


# ------> String data types

st1 = 'student of A.c patil college'
print(st1)

st2 = "student of A.c patil college"
print(st2)

st3 ='''student of A.c patil college'''
print(st3)

# ------> string opertaion

# 1]  Slice([] & [:]) 

Value = "Hello Duniya !!"
print(Value[:5])
Value = "Hello Duniya !!"
print(Value[1:4])
Value = "Hello Duniya !!"
print(Value[1:3:2])

# => Negative Indexing

al = "Hello Duniya "
print(al[-5:-2])


# 2] Concatenation (+) 

str1="Hello Duniya"
str2=" Namaste Duniya"
# print ("String 1:",str1)
# str1=str1*3
strv3 = str1+ str2
print("Concatenated same string:",strv3)

# 3] Repetition(*):

rep = ' This is the Python program '
print(rep*3)

