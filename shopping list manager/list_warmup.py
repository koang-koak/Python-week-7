# 1. Create a list called fruits containing four fruits of your choice
fruits = ["apple", "banana", "mango", "orange"]

# 2. Print the first and the last item using indexes
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Append a fifth fruit, then print the whole list
fruits.append("pineapple")
print("After adding a fruit:", fruits)

# 4. Remove one fruit, then print the list again
fruits.remove("banana")
print("After removing a fruit:", fruits)

# 5. Print how many fruits remain using len()
print("Number of fruits remaining:", len(fruits))