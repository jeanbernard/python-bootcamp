print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
photo_price = 3
child = 5
teen = 7
adult = 12
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    
    age = int(input("What is your age? "))
    if age < 12:
        print(f"Child ticket is ${child} amigo.")
        bill = child
    elif age <= 18:
        print(f"Teen ticket is ${teen} amigo.")
        bill = teen
    elif age < 45:
        print(f"Adult ticket is ${adult} amigo.")
        bill = adult
    elif age >= 45 and age <= 55:
        print(f"free ticket amigo!")
    photo = input("Do you want a photo amigo? ")
    if photo == 'y':
        print(f"Pay ${photo_price} extra amigo")
        bill += photo_price
    
    print(f"Bill total is ${bill}")
else:
    print(f"Sorry, no dice! You're too short amigo {height}")
