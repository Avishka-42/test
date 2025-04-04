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
