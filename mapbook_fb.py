from not1 import add_user
from utils.model import users
from utils.controller import get_user_info, add_user


def main():
    print(f'Witaj {users[0]['name']}')

    while True:
        print('===========MENU===========')
        print('0 - zakończ program')
        print('1 - pokaż co u znajomych')
        print('2 - dodaj nowego znajomego')
        print('3 - usuń znajomego')
        print('==========================')
        choice = input('wybierz opcję MENU: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': users.pop()


if __name__ == '__main__':
    main()
