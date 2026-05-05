# splitting strings into multiple variables
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

print(f"hello, {name}")