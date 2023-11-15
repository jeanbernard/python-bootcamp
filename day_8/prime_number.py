# Write your code below this line 👇
def prime_checker(number):
  is_prime_number = True
  for i in range(2, number):
    is_clean_division = number % i == 0

    if is_clean_division:
      is_prime_number = False
      break

  if is_prime_number:
    return "It's a prime number."
  else:
    return "It's not a prime number."
    
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input()) # Check this number
# prime_checker(number=n)