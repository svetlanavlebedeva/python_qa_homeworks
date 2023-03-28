import csv
import json
import os


def func_ex8():
    def csv_reader(file_url):

        abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_url)
        return csv.DictReader(open(abs_path))

    def json_reader(file_url):

        abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_url)
        return json.load(open(file_url))

    user_list = json_reader("users.json")
    book_list = csv_reader("books.csv")

    users = [
        {
            "name": x["name"],
            "gender": x["gender"],
            "address": x["address"],
            "age": x["age"],
            "books": [],
        }
        for x in user_list
    ]

    while True:
        try:
            for i in users:
                book = next(book_list)
                i["books"].append(
                    {
                        "title": book["Title"],
                        "author": book["Author"],
                        "pages": book["Pages"],
                        "genre": book["Genre"],
                    }
                )
        except StopIteration:
            break

    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "result.json"), "w"
    ) as f:
        f.write(json.dumps(users, indent=4))


func_ex8()
