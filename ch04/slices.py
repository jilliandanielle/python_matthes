cubes = []
for value in range(1,11):
    cubes.append(value**3)

print(f"The first three items in the list are: {cubes[0:3]}")

print(f"Three items from the middle of the list are: {cubes[3:6]}")

print(f"The last three items in the list are: {cubes[7:]}")
