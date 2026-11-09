#1
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


#2
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


#3
def print_substring_reverse(s, start, finish):
    if s is None or s.strip() == "":
        print("Wrong args")
        return
    if start<0 or finish>=len(s) or start>finish:
        print("Wrong args")
        return
    beginning = s[:start]
    middle_reverse = s[start:finish+1][::-1]
    end_reverse = s[finish+1:]
    print(beginning+middle_reverse+end_reverse)

print_substring_reverse("Shalom",1,3)
print_substring_reverse(None,1,3)
print_substring_reverse("Hi",1,5)
print_substring_reverse("Hi",3,1)



#4
def get_words_reverse(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
print()
print(get_words_reverse("Hello my nice world"))

def print_words_reverse_in_column(s):
    words = s.split()
    for word in words:
        print(word[::-1])
print_words_reverse_in_column("Hello my nice world")

