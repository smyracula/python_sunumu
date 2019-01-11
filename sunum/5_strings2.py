x = "Arkadaşım Eşek"
print(x.index("ı"))

#ErrorCase:
#print(x.index("ıssada"))

#Hata yaşanmaması için find kullanılmalıdır.
#print(x.find("ıssada"))

if x.find('ı') > 0:
    print(x.find("ı"))
else:
    print("bulunamadı")


if x.find('asdası') > 0:
    print(x.find("asdası"))
else:
    print("bulunamadı")
