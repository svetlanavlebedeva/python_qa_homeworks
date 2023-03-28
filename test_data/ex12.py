import json
import csv

result = []

with open("users.json", "r") as file:
    users = json.load(file)
    for user in users:
        result.append(
            {'name': user['name'],
             'gender': user['gender'],
             'address': user['address'],
             'age': user['age'],
             'books': []
             }
        )

with open("books.csv", "r") as file:
    books = csv.DictReader(file)

    i = 0

    for book in books:
        result[i % len(result)]['books'].append(
            {
                'title': book['Title'],
                'author': book['Author'],
                'pages': book['Pages'],
                'genre': book['Genre']
            }
        )
        i += 1

with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)
