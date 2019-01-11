def add(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam = toplam + sayi
    return toplam

print(add(1,2,4,5,4,2,1))

input("Devam için enter")

# ** ifadesi Dictionary ifade eden veri tipidir.
def sampleDictionary(**kwargs):
    for key,value in kwargs.items():
        print("{} - {}".format(key,value))


sampleDictionary(BestPlayer = "Lebron James",BestRookiePlayer = "Luka Doncic")
s
