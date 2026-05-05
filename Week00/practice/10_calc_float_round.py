# float casting, rounding, and formatting with comma separators
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")