simple intrest.

p = int (input('enter the principal'))
t = int (input('enter the time'))
r = int (input('enter the rate'))
print((p*t*r)/100)

square of number.

n = int(input('enter the no'))
s = n*n
print(s)

arithemetic operators.

a = int(input('enter the value of a'))
b = int(input('enter the value of b'))
c = a+b
print(c)
c = a-b
print(c)
c = a*b
print(c)
c = a/b
print(c)
c = a%b
print(c)
c = a||b
print(c)
c = a**b
print(c)

assignment operator.

a = int(input('enter the value of a'))
a = a+5
print(a)
a = a-5
print(a)
a = a*5
print(a)
a = a%5
print(a)
a = a||5
print(a) 

input two numbers and swap them.

name1 = str(input("enter the name1"))
name2 = str(input("enter the name2"))
print("name1 is",name1,"name2 is",name2)
name1,name2 = name2,name1print("name1 is",name1,"name2 is",name2)

make a simple calculator.

def calculator():
num1 = float(input("enter first no:"))
operator = input("enter operator(+,-,*,/):")
num2 = float(input("enter second no:"))
match operator:
case "+":
result = num1+num2
case "-":
result = num1-num2
case "*":
result = num1*num2
case "/":
if num2 ! = 0:
result = num1/num2
else:
print("error:division by zero is not allowed!")
return
case _:
print("error:invalid operator!")
return
print(f "result:{result}")
calculator()

