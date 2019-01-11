
while True:
    rakam = input("Lütfen bir rakam giriniz\n")
    if(rakam.isdigit()):
        break
    else:
        print("Girilen değer bir rakam değildir.")
    
if int(rakam) > 100:
    print("Rakam 100'den büyüktür.")
elif int(rakam) < 10:
    print("Rakam 10'dan küçüktür.")
else:
    print("Rakam 10 ile 100 arasında bir değerdir")
