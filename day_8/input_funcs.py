name = "JJ"
location = "Dominican Republic"

def greet_with_name(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")
greet_with_name(name)

print("")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#Positional arguments
greet_with(name, location)

# Keyword arguments
greet_with(location="DR", name="JeanB")