import re

text = "The test status is passed"
result  = re.search("passed",text)
print(result)
print(result.group())


text1 = "passed: test_login"
text2 = "test_login: passed"
print(re.match("passed",text1))
print(re.match("passed",text2))

print(re.fullmatch("passed","passed"))
print(re.fullmatch("passed","passed!"))

print(re.search("c.t","cat"))
print(re.search("c.t","cut"))
print(re.search("c.t","ct"))

result = re.search("^Test",text)
if result:
    print(result.group())
else:
    print("Not found")

print(re.search("passed$","test_login: passed"))
print(re.search("passed$","passed: test_login"))

print(re.search("gr[ae]y","grey"))
print(re.search("gr[ae]y","gray"))
print(re.search("gr[ae]y","gree"))

print(re.search("[A-Za-z]","hello world"))
print(re.search("[^0-9]","12345a"))
print(re.search("[^0-9]","12345"))

print(re.search(r"\d","Order #42"))
print(re.search(r"\w","!!!hello"))
print(re.search(r"\s","no spaces here"))
