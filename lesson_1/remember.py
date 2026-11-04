age = 25
name = 'Kristina'

#int - целые числа
#float -дробные числа
#str- строки
#bool - логический

said = "'She said 'Hello'"
print(said)

my_string = '''This is a multy-line string.
We've wrapped the text to the next line'''
print(my_string)

raw_string = r"C:\Program Files\Kristina\Python"
print(raw_string)

s1 = "Hello Kris"
print(type(s1))
s2 = 5
print(type(s2))
s3 = True
print(type(s3))
s4 = 2.0
print(type(s4))

s5 = 'Zeleno'
s6 = 'glazka'
s7 =  s5 + s6
print(s7)

#join()
words = ["Hello", "World", "and", "Python"]
res = " ".join(words)
print(res)

st = "ab" * 7
print(st)

st1 = 35 * '*'
print(st1)

s1 = 'Kris Tomash'
s2 = 'Kristina'

if s2 in s1:
    print("User Kristina is in a DB")
else:
    print("User Kristina is not in a DB")

st = 'a'
if st == 'a' or st == 'b' or st == 'c' or st == 'd':
    print("Yes")

if st in 'abcd':
    print("Yes")


#********************************
#len()
ln = len('Zelenoglazka')
print(ln)
s1 = 'Zelenoglazka'
print(len(s1))

#**********************************
#0 1 2 3 4 5
#P Y T H O N

st = 'Python'
print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])

#-6 -5 -4 -3 -2 -1
#P  Y  T  H  O  N
st = 'Python'

print(st[-1])
print(st[-2])
print(st[-3])
print(st[-6])

st = 'Python'

print(st[0:3])
print(st[2:5])
print(st[4:6])

my_string = "Hello world"
every_second_char = my_string[::2]
print(every_second_char)
from_second = my_string[1::2]
print(from_second)
my_substring = my_string[1:10:3]
print(my_substring)

reversed_string = my_string[::-1]
print(reversed_string)