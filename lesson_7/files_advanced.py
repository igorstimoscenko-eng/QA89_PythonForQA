def save_shopping_list(items):
    with open("shopping.txt","w",encoding="utf-8") as file:
        for item in items:
            file.write(item+"\n")
items = [
    "milk",
    "bread",
    "apples",
    "coffee"
]
save_shopping_list(items)

with open("shopping.txt","r",encoding="utf-8") as file:
    print(file.read())