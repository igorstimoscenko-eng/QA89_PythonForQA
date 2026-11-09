def print_string_reverse(s):
    if s is None or s.strip() == "":
        print("Wrong String")
        return
    #else:
       #print (s[::-1])
    reversed_s = s[::-1]
    print(reversed_s)

print_string_reverse("Shalom")
print_string_reverse(None)
print_string_reverse("")
print_string_reverse(" ")