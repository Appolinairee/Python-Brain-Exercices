animals = ["vache", "souris", "levure", "bacterie"]

for i in range(len(animals)):
    print(animals[i], end=" ")
    
print("\n")
    
for animal in animals:
    print(animal, end=" ")

print("\n")    

index = 0
while index < len(animals):
    print(animals[index], end=" ")
    index += 1