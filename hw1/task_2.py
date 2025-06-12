foods = ("apple","banana","orange","mango","strawberry","grape","mandarin","strawberry")
calories = (52,96,62,605,33,68,50,33)

foods_list = list(foods)
calories_list = list(calories)

print (foods)
print (calories)

print (foods_list)
print (calories_list)

print (foods [4],calories [4])

print (foods [-2],calories [-2])

foods_u = list(set(foods))
calories_u = list(set(calories))
print(foods_u)
print(calories_u)

foods_d = dict(zip(foods,calories))
print (foods_d)