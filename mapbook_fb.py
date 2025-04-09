users:list=[
    {'name':'Filip','location':'Sieradz','posts:':2},
    {'name':'Oliwier','location':'Zamość','posts:':3},
    {'name':'Jakub','location':'Warszawa','posts:':500},
    {'name':'Konrad','location':'Lublin','posts:':10},
]


def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'witaj {user['name']}')

def get_user_info(users)