import csv
import json
import time


def func_ex6():
    # read csv file
    with open("books.csv", "r") as f:
        books = csv.DictReader(f)
        books = [i for i in books]

    # read json file
    with open("users.json", "r") as f:
        users = json.load(f)

    # created new user list with the keys ['name', 'gender', 'address', 'age', 'books']
    users_result = []

    for user in users:
        user_res = {
            key: value
            for key, value in user.items()
            if key in ["name", "gender", "address", "age", "books"]
        }
        user_res["books"] = []
        users_result.append(user_res)

    # sharing books to users
    while books:
        for user_res in users_result:
            if books:
                user_res["books"].append(books.pop())
            else:
                break

    # save result to result.json
    with open("result.json", "w") as f:
        json.dump(users_result, f, indent=4)


func_ex6()
