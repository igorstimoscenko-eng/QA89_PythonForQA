import json

#dumps() Python-> JSON строку( работает со строкой)
#loads() текст JSON -> Python обьект
#dump() - > Python -> file format JSON.file(работа с файлом)
#load()  JSON.file -> Python(работа с файлом)

user = {"username":"Kristina","age": 39,"is admin":True}
json_string = json.dumps(user)
print(json_string)
print(type(json_string))

user = json.loads(json_string)
print()
print(user)
print(type(user))
print(user["username"])