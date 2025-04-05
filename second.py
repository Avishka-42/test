factorization methos.

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
  while n % i == 0:
            factors.append(i)
            n //= i
    return factors
  

wheather the no is even or odd.

while true:
num = int(input("enter a number(0 to exit):"))
if num == 0:
    print("exiting the program.")
    break
if num%2 == 0:
    print("even number")
else:
    print("odd number")


calculate the cube root of all odd numbers upto 10 also find sum of them.

i=0
sum=0
while i<=10:
    print("its even",i)
else:
    c = i**3
    print("its odd",e)
    sum = sum+c
    i+ = 1
    print (sum)

factorial of a number using function.

def factorial(n):
    if n==0 or n==1;
    return 1
else:
return n*factorial(n-1)
num = int(input("enter a no:"))
result = factorial(num)
print(f"the factorial of {num} is {result}")

calculate positive integer using function.

def sum_positive_integer(n):
    total = 0
    for i in range(1,n+1):
        total + = i
        return total
    n = int(input("enter the no of positive integers to sum"))
result = sum_positive_integer(n)
print(f"the sum of the first {n} positive integers is {result}")
