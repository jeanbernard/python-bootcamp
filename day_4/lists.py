states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
states[1] = "Pencilvania"
states.append("Angelaland")
states.extend(["A", "B", "C"])
print(states)

fruits = ["Apples", "Grapes", "Peaches"]
vegetables = ["Potatoes", "Kale", "Spinach"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[1][1])
dirty_dozen[1][1] = "Kales"
print(dirty_dozen[1][1])