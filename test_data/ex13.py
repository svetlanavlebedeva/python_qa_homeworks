import csv
import json

result = []
with open('books.csv', 'r', newline='') as csv_file, open('users.json', 'r') as json_file:
    for user in json.load(json_file):
        result.append(
            {
                'name': user['name'],
                'gender': user['gender'],
                'address': user['address'],
                'age': user['age'],
                'books': []
            }
        )

    iter_result = iter(result)
    for book in list(csv.DictReader(csv_file)):
        try:
            person = next(iter_result)
            person['books'].append(
                {
                    'title': book['Title'],
                    'author': book['Author'],
                    'pages': int(book['Pages']),
                    'genre': book['Genre']
                }
            )
        except StopIteration:
            iter_result = iter(result)

with open('result.json', 'w') as output_json:
    output_json.write(json.dumps(result, indent=2))
