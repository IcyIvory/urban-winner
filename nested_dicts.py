users = {
    'pgarden': {
        'first_name': 'pylot',
        'last_name': 'garden',
        'age': '20',
        'city': 'halifax'
    },
    'dotoole': {
        'first_name': 'doc',
        'last_name': "o'toole",
        'age': '46',
        'city': 'haliburton'
    },
    'whouston': {
        'first_name': 'windy',
        'last_name': 'houston',
        'age': '32',
        'city': 'houston'
    }
}

for username, info in users.items():
    print(f'\nUsername: {username}')
    full_name = f"{info['first_name'].title()} {info['last_name'].title()}"
    location = info['city'].title()

    print(f"{full_name}, age {info['age']}, of {location}")
