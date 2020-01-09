username = ['Jillian', 'Danielle', 'Bernadette', 'Mary', 'Kristine', 'admin']

for name in username:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")

    else:
        print(f"Hello {username}, thank you for logging in again.")