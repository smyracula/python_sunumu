def subt(x,y):
    return x-y

def deneme(text):
    a = 1
    b = 4
    print(text,"-", a,"-",b)

#default parametreler mutlaka sonda bulunmadır. Runtime hatası alırsınız yoksa
def info(isim,sehir,hayvan = "Kedi"):
    print("Merhaba, ben {}, doğduğum şehir {} ve {} severim".format(isim,sehir,hayvan))
    
subtract_result = subt(2,9)
print("sonuç={}".format(subtract_result))

input("Devam için enter")

subtract_result = subt(y = 2,x = 9)
print("sonuç={}".format(subtract_result))

input("Devam için enter")

text = "deneme"
a = 3
b = 98
print(deneme(text))
print(text,"-", a,"-",b)

#yukarıdaki kod parçacağında değişken isimleri aynı gibi görünse de deneme fonksiyonundaki a ve b değerleri local scope olduğu için program içindeki a ve b değerlerinden bağımsızdır.
input("Default parametreler için enter")
info("Korcan","İzmir")
info("Melih","Bangladeş","İnek")
