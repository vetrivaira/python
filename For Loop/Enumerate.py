# Using enumerate to access index values
print("Using enumerate:")
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Using range to access index values
print("\nUsing range:")
for index in range(len(fruits)):
    print(f"Index: {index}, Fruit: {fruits[index]}")