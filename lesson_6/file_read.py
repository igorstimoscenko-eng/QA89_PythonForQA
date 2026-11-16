with open("users.txt","w",encoding="utf-8") as file:
    file.write("Lora\n")
    file.write("Ivan\n")
    file.write("Kris\n")

#read()-> all file
with open("users.txt","r",encoding="utf-8") as file:
    content = file.read()
print(content)
print(len(content))

#readlines()
with open("users.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
print(lines)
print(lines[0])
for line in lines:
    print(line.strip())
print()

#for
with open("users.txt","r",encoding="utf-8") as file:
    for line in file:
        print(line.strip())