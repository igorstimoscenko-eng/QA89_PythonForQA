def login(username,password):
    print(username,password)

data = ['admin',"123456"]
login(data[0],data[1])

(login(*data))

user = {
    "username":"admin",
    "password":"A12345"
}
login(**user)

user = {
    "username":"admin",
    "password":"A12345",
    # "remember_me":True
}
login(**user)