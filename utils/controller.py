def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów.') \
 \
        new_name = input('podaj imie nowego znajomego:')
        new_location = input('podaj miasto nowego znajomego:')
        users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts})
        add_user(users)

        print(users)
