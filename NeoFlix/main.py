from fitur import User


users = [
    User("alice", "Basic", 6, "REF123"),
    User("bob", "Premium", 12, "REF456"),
    User("charlie", "Standard", 3, "REF789")
]

user1 = User('user1', 'Basic', 10, 'REF789')

print('\n=====================')
print('Selamat datang di NeoFlix')
print('=====================')

while True:
    print('\n=====================')
    print('1. Lihat plan yang kamu miliki')
    print('2. Beli plan')
    print('3. Lihat seluruh plan NeoFlix')
    print('4. Keluar')
    print('=====================')
    menu = input('Pilih menu: ')

    if menu == '1':
        user1.get_user_plan()
    elif menu == '2':
        user1.buy_plan(users)
    elif menu == '3':
        for key in range(3):
            user1.get_plan(key)
    elif menu == '4':
        print('Terima kasih telah menggunakan NeoFlix')
        break
    else:
        print('Menu tidak tersedia')
