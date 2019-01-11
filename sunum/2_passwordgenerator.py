import random

s="abcdefghijklmnoprstuvyzxw1234567890ABCDEFGHIJKLMNOPRSTUVYZWX!@#&%<>*()"

passwordlenght = 8

p = "-".join(random.sample(s,passwordlenght))

print(p)
