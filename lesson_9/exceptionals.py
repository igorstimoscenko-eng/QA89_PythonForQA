#with open("user.json","r",encoding="utf-8") as file:
# print(file.read())

# print("Start program")
# result = 10/0
# print(result)
# print("End program")

# def div_int(a,b):
#     return a/b
#
# print("Start program")
# res = div_int(10,0)
# print(res)
# print("End program")
# print()

#try/except
print("Start program")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("An error occured: ",e)
print("End program")

def is_number(text):
    try:
        float(text)
        return True
    except (ValueError, TypeError):
        return False

print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Hello"))
print(is_number(None))