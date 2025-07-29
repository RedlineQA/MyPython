print("Please enter your full name")
fullname = input()
print("Choose your flight destination")
destination = input()
print("Choose your seat")
seat = input()
index = fullname.index(" ")
first_name = fullname[0:index]
last_name = fullname[index + 1:]
first_name_len = len(first_name)
last_name_len = len(last_name)
fullname_len = len(first_name) + len(last_name)
print(f"Hello {fullname}!")
print(f"Your flight to {destination} is confirmed.")
print(f"Seat number: {seat}")
print(f"Your first name has {first_name_len} letters, and your last name has {last_name_len} letters.")
print(f"Total characters in your full name: {fullname_len}")
if first_name_len > last_name_len:
    difference = first_name_len - last_name_len
    print(f"Your first name is longer than your last name by {difference} characters.")
elif last_name_len > first_name_len:
    difference = last_name_len - first_name_len
    print(f"Your last name is longer than your first name by {difference} characters.")
else:
    print(f"Both your first name and your last name have the same number of characters.")
