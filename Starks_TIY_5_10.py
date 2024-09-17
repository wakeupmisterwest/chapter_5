# This program simulates how websites ensure that everyone has a unique username
current_users = ['mango', 'catlover43', 'ratlobber', 'thelegend27',
                 'bakedbeanlover23']
new_users = ['ratlobber', 'MANGO', 'spacepanda', 'beesmakehoney', 'whatthecat']


current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is unavailable. Enter a new username.")
    else:
        print(f"{new_user} is available.")
