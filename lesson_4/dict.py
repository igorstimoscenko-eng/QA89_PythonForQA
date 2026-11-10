books = {
    'Harry Potter and .....':'J.K.Rowling',
    'To kill a mockingbird':'Harper Lee'
}

books1 = {
    'Harry Potter and .....',
    'To kill a mockingbird'
}
print(books1)

response = {
    'statusCode': 'success',
    'user': {
        'id':1,
        'name':'Kris'
    }
}

#API

contact = {
    "id":12,
    "name":"Anna",
    "email":"anna@gm.com"
}
req_field = {
    "id",
    "name",
    "email"
}
for field in req_field:
    assert field in contact, f"В ответе отсутствует поле{field}"