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

test_config = {
    "base_url": "http://127.0.0.1:8000",
    "timeout": 10,
    "retries": 3
}

with open("config.json", "w") as file:
    json.dump(test_config, file, indent=4, ensure_ascii=False)

with open("config.json", "r") as file:
    loaded_config = json.load(file)
print(loaded_config)
print(loaded_config["base_url"])