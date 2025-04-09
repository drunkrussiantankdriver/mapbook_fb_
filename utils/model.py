users: list = [
    {'name': 'Bartlomiej', 'location': 'Lublin', 'posts': 2},
    {'name': 'Oliwier', 'location': 'Zamość', 'posts': 3},
    {'name': 'Kuba', 'location': 'Warszawa', 'posts': 500},
    {'name': 'Konrad', 'location': 'Lublin', 'posts': 10},
]
print(users)


def remove_user(users_data: list) -> None:
    user_tbr = input('podaj nazwę znajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == 'Bartlomiej':
            users_data.remove({'name': 'Bartłomiej', 'location': 'Lublin', 'posts': 2})


remove_user(users)
print(users)
