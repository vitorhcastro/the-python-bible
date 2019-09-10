# Ask user for name
name = input("What is your name?\n")

# Ask user for age
age = input("What is your age?\n")

# Ask user for city
city = input("What is your city?\n")

# Ask user what they enjoy
love = input("What do you love doing?\n")

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name, age, city, love)

# Print output text
print(output)
