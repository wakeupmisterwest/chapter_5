# This program greets each user after they log in.
usernames = ['admin', 'catlover43', 'ratlobber', 'thelegend27', 'beanlover23']


for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
