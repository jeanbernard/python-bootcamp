print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
sp = 15
mp = 20
lp = 25
isSmallPizza = size == 'S'
isMediumPizza = size == 'M'

if isSmallPizza:
  bill += sp
elif isMediumPizza:
  bill += mp
else:
  bill += lp
  
if add_pepperoni == 'Y':
    if isSmallPizza:
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
  bill += 1

print(f"Your final bill is: ${bill}.")