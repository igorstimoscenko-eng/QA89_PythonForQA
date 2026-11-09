# Quest 1704: python-ru-1704-inrerview-ap
#
# 1. Написать функцию print_string_reverse(s)
# Функция принимает строку и выводит эту строку в консоль в обратном порядке.
# Если строка равна None, пустая или состоит только из пробелов, функция должна вывести:
# Wrong string
# Пример:
# print_string_reverse("Shalom")
# Вывод в консоль:
# molahS
# *****************************************
#
# 2. Написать функцию is_isr_phone_number(phone)
# Функция принимает строку и проверяет, является ли она израильским номером телефона.
# Условия корректного номера:
# первая цифра — 0;
# общее количество символов — 10;
# все символы являются цифрами.
# Если строка соответствует всем условиям, функция возвращает True.
# Если строка не соответствует условиям, функция возвращает False.
# Если строка равна None, пустая или состоит только из пробелов, функция возвращает None.
# Примеры:
# is_isr_phone_number("0521234567") → True
# is_isr_phone_number("521234567") → False
# is_isr_phone_number("05212345a7") → False
# is_isr_phone_number("") → None
#
# 3. Написать функцию print_substring_reverse(s, start, finish)
# Функция принимает строку, стартовый индекс и финишный индекс.
# Нужно вывести в консоль строку, в которой символы от индекса start до индекса finish
# включительно напечатаны в обратном порядке, а остальные символы остаются в обычном порядке.
# Пример:
# print_substring_reverse("Shalom", 1, 3)
# Исходная строка:
# Shalom
# Часть строки от индекса 1 до индекса 3 включительно:
# hal
# После реверса:
# lah
# Вывод в консоль:
# Slahom
# Если строка равна None, пустая или состоит только из пробелов, или индексы start / finish
# выходят за пределы строки, или start > finish, функция должна вывести:
# Wrong args
#
# 4. Advanced
# Написать функцию get_words_reverse(s)
# Функция принимает строку, где слова разделены пробелами, и возвращает исходную строку
# в обратном порядке слов.
# Пример:
# get_words_reverse("Hello my nice world")
# Результат:
# world nice my Hello
#
# Advanced
# Написать функцию print_words_reverse_in_column(s)
# Функция принимает строку, где слова разделены пробелами, и выводит в консоль слова в столбик.
# Каждое слово должно быть выведено задом наперед.
# Пример:
# print_words_reverse_in_column("Hello my nice world")
# Вывод в консоль:
# olleH
# ym
# ecin
# dlrow


def is_blank(s):
    return s is None or not s.strip()


def print_string_reverse(s):
    if is_blank(s):
        print("Wrong string")
        return
    print(s[::-1])


def is_isr_phone_number(phone):
    if is_blank(phone):
        return None
    return len(phone) == 10 and phone.isascii() and phone.isdigit() and phone[0] == "0"


def print_substring_reverse(s, start, finish):
    if is_blank(s) or not (0 <= start <= finish < len(s)):
        print("Wrong args")
        return
    print(s[:start] + s[start:finish + 1][::-1] + s[finish + 1:])


def get_words_reverse(s):
    if is_blank(s):
        return ""
    return " ".join(s.split()[::-1])


def print_words_reverse_in_column(s):
    if is_blank(s):
        return
    for word in s.split():
        print(word[::-1])


if __name__ == "__main__":
    print_string_reverse("Shalom")
    print_string_reverse("   ")
    print("*" * 41)

    print(is_isr_phone_number("0521234567"))
    print(is_isr_phone_number("521234567"))
    print(is_isr_phone_number("05212345a7"))
    print(is_isr_phone_number(""))
    print("*" * 41)

    print_substring_reverse("Shalom", 1, 3)
    print_substring_reverse("Shalom", 3, 1)
    print_substring_reverse("Shalom", 0, 6)
    print("*" * 41)

    print(get_words_reverse("Hello my nice world"))
    print("*" * 41)

    print_words_reverse_in_column("Hello my nice world")
