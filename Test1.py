s = {}
print(s)
print("\n")

s = {
    "1":    123,
    "2":    "abc",
    "3":    456,
    }

s["4"]          =   "aaa"
s["5"]          =   "qwerty"
s["6"]          =   123

print(s)

print("\n")
for a,b in s.items():
    print(str(a) + "\t" + str(b))

print("\n")
for a in s:
    print(a)

print("\n")
print(s.values())

print("\n")
print(s.keys())

print("\n")
print(s.popitem())
print(s.popitem())
print(s.popitem())