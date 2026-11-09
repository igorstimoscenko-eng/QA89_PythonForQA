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


def is_isr_phone_number(phone):
    if phone is None or phone == "":
        return None
    if len(phone) != 10:
        return False
    if phone[0] !="0":
        return False
    if not phone.isdigit():
        return False
    return True

#print()
test_input = input("Enter a phone number: ")
first_number = is_isr_phone_number(test_input)
print(first_number)

#print(is_isr_phone_number("0521234567"))
#print(is_isr_phone_number("521234567"))
#print(is_isr_phone_number("05212345a7"))
#print(is_isr_phone_number(""))