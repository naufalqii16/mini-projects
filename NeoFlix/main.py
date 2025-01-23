from fitur import User

users = [
    User("alice", "Basic", 6, "REF123"),
    User("bob", "Standard", 13, "REF456"),
    User("charlie", "Standard", 3, "REF789")
]

new_user = User('anak baru', None, 0, 'REF789')
mid_user = users[0]
old_user = users[1]

trial_users = [ new_user, mid_user, old_user ]

print('\n=====================')
print('Login to NeoFlix')
print('=====================')
while True:
    user_type = int(input('What kind of user are you?:\n1. new user\n2. mid user\n3. old user\npick number: '))
    if user_type not in [1,2,3]:
        print('pick the right number\n')
        continue
    break
    
print('\n\n=====================')
print(f'Welcome to NeoFlix, {trial_users[user_type-1]}')
print('=====================')

while True:
    print('\n=====================')
    print('1. Check my plan')
    print('2. Buy plan')
    print('3. Upgrade plan')
    print('4. Check all plan of NeoFlix')
    print('5. Exit')
    print('=====================')
    menu = input('Pick menu: ')
    print('---------------------')

    if menu == '1':
        trial_users[user_type-1].get_user_plan()
    elif menu == '2':
        trial_users[user_type-1].buy_plan(users)
    elif menu == '3':
        trial_users[user_type-1].upgrade_plan()
    elif menu == '4':
        trial_users[user_type-1].get_plan(4)
    elif menu == '5':
        print('Thank you for using NeoFlix')
        break
    else:
        print('Menu isn\'ot available')
