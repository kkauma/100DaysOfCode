def prime_checker(number):
  is_prime = True
  for i in range(2, int(number/2)+1):
    if (number % i) == 0:
      is_prime = False
      break
  if is_prime and number != 1:
    print(f"{number} is a prime number.")
  else:
    print(f"{number} is not a prime number.")

n = int(input("Enter a number: "))
prime_checker(number=n)