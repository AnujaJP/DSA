##Ask the user for their birth year (as string), convert it to integer, calculate their age in 2025 and print:
##"You will be X years old in 2025!" (X = 2025 - birth_year)

BIRTHYEAR = input("Enter your birth year: ")
converted = int(BIRTHYEAR)
X = 2025 - converted
print("You will be", X, "years old in 2025!")
