"""
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'Audi'? I predict False.")
print(car == "Audi")
"""

"""
alian_colors = ["green", "yellow", "red"]
for alian_color in alian_colors:
    if alian_color == "green":
        print("You have earned 5 points")
    elif alian_color == "yellow":
        print("You have earned 10 points")
    else:
        print("You have earned 15 points")
"""

"""
age = 32
if age < 2:
    print("The person is a baby")
elif age >= 2 and age < 4:
    print("The person is a toddler")
elif age >= 4 and age < 13:
    print("The person is a kid")
elif age >= 13 and age < 20:
    print("The person is a teenager")
elif age >= 20 and age < 65:
    print("The person is an adult")
else:
    print("The person is an elder")
"""
"""
users = ["admin", "user1", "user2", "user3", "user4"]
if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")
"""

"""
current_users = ["user1", "user2", "user3", "user4", "user5"]
new_users = ["User1", "user6", "User7", "user2", "user8"]
for new_user in new_users:
    if new_user.lower() in [current_user for current_user in current_users]:
        print(
            f"Sorry {new_user}, that username is already taken. Please enter a new username."
        )
    else:
        print(f"Congratulations {new_user}, that username is available.")
"""

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
