import csv
import json

def read_students(filename):
    with open(filename,"r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']} ({row['age']})")
read_students("students.csv")

def save_profile(name, age, city):
    profile = {
    "name": name,
    "age": age,
    "city": city
}
    with open("profile.json","w",encoding="utf-8") as file:
        json.dump(profile,file,indent=4)

    with open('profile.json', 'r') as file:
        print(json.load(file))

save_profile("Maria", "30", "Haifa")