from gui import add_user
from utils.tk_crud import users
from utils.crude import get_user_info, add_user, edit_user, users.pop


def main():
    print(f'Witaj {users[0]['name']}')

    while True:
        print('===========MENU===========')
        print('0 - zakończ program')
        print('1 - pokaż co u znajomych')
        print('2 - dodaj nowego znajomego')
        print('3 - usuń znajomego')
        print('4 - edytuj znajomego')
        print('==========================')
        choice = input('wybierz opcję MENU: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': users.pop()
        if choice == '4': edit_user(users)



    main()
