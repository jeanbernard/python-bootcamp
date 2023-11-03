print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t") + lower_names.count("r") + lower_names.count("u") + lower_names.count("e")
l = lower_names.count("l") + lower_names.count("o") + lower_names.count("v") + lower_names.count("e")

love_score = str(t) + str(l)
love_score = int(love_score)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
