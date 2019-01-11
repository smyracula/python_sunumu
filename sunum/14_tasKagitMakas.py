from random import randint

t= ["Taş","Kağıt","Makas"]

oyuncu_skoru = 0
bilgisayar_skoru = 0
el_sayisi = 0

while oyuncu_skoru < 2 and bilgisayar_skoru < 2:
    bilgisayar = t[randint(0,2)]
    el_sayisi = el_sayisi +1
    oyuncu=input("Taş, Kağıt, Makas?\n")
    if oyuncu == bilgisayar:
        print("Bu el berabere")
    elif oyuncu == t[0]:
        if bilgisayar == t[1]:
            print("{} {}'ı sarar. Bu eli bilgisayar kazandı!".format(t[1],t[0]))
            bilgisayar_skoru = bilgisayar_skoru + 1
        else:
            print("{} {}'ı kırar. Bu eli sen kazandın!".format(t[0],t[2]))
            oyuncu_skoru = oyuncu_skoru + 1
    elif oyuncu == t[1]:
        if bilgisayar == t[0]:
            print("{} {}'ı sarar. Bu eli sen kazandın!".format(t[1],t[0]))
            oyuncu_skoru = oyuncu_skoru + 1
        else:
            print("{} {}'ı keser. Bu eli bilgisayar kazandı!".format(t[2],t[1]))
            bilgisayar_skoru = bilgisayar_skoru + 1
    elif oyuncu == t[2]:
        if bilgisayar == t[0]:
            print("{} {}'ı kırar. Bu eli bilgisayar kazandı!".format(t[0],t[2]))
            bilgisayar_skoru = bilgisayar_skoru + 1
        else:
            print("{} {}'ı keser. Bu eli sen kazandın!".format(t[2],t[1]))
            oyuncu_skoru = oyuncu_skoru + 1
    else:
        print("{}, {}, {} arasında bir tercihte bulununuz".format(t[0],t[1],t[2]))
    print("Skor\nOyuncu : {} \nBilgisayar : {}".format(oyuncu_skoru,bilgisayar_skoru))
    print("-------------------------------------------------")

print("Oyun Bitti!\n{} el sonunda skorlar\nOyuncu : {} \nBilgisayar : {}".format(el_sayisi,oyuncu_skoru,bilgisayar_skoru))
if bilgisayar_skoru > oyuncu_skoru:
    print("Üzgünüm. Kaybettin :(")
else:
    print("Sen Kazandın. Tebrikler!")



