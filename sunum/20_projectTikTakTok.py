import random
import sys

#bu fonksiyonun amacı python 3.0 altında bir versiyonda bu programı çalıştırırsanız hata almaması için.
def girdi_al():
	if sys.version_info >= (3, 0):
		return input()
	else:
		return raw_input()

def tahtayiCiz(oyunTahtasi):
    # fonksiyona gönderilen oyun tahtasını ekrana basar
    # oyunTahtasi dizisinde gerekli kontrollerin kolay yapılabilmesi için 0. index boş bırakılmıştır.
    print(' ' + oyunTahtasi[7] + ' | ' + oyunTahtasi[8] + ' | ' + oyunTahtasi[9])
    print('-----------')
    print(' ' + oyunTahtasi[4] + ' | ' + oyunTahtasi[5] + ' | ' + oyunTahtasi[6])
    print('-----------')
    print(' ' + oyunTahtasi[1] + ' | ' + oyunTahtasi[2] + ' | ' + oyunTahtasi[3])

def oyuncununHarfiniAl():
    # oyuncunun temsil edileceği X veya O harfi girdi olarak alınır
    # harf girdisi X ve O olana kadar girdi istenir. Küçük harf girilirse büyük harfe çevrilir.
    harf = ''
    while not (harf == 'X' or harf == 'O'):
        print('Hangisi olmak istersin\nX or O?')
        harf = girdi_al().upper()

    # 2 adet eleman içeren bir dizi döndürülür. İlk harf oyuncuyu ikinci harf bilgisayarı temsil eder.
    if harf == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def yaziTura():
    # ilk kim başlayacak?
    if random.randint(0, 1) == 0:
        return 'bilgisayar'
    else:
        return 'oyuncu'

def yenidenOyna():
    # Oyuncudan yeniden oynamak isteyip istemediğine dair bir yanıt alınıyor. Yanıt E ile başlarsa oyun yeniden başlıyor.
    print('Yeniden oynamak ister misin? (evet ya da hayır)')
    return girdi_al().lower().startswith('e')

def hamleYap(tahta, harf, hamleNoktasi):
    if bosAlanMi(tahta,hamleNoktasi):
        tahta[hamleNoktasi] = harf
    else:
        raise Exception("hamleYap: alan boş olamaz!")

def kazandimi(bo, le):
    # Oyun tahtası ve kimin hamlesi ise hamleden sonra onun harfi bu fonksiyona yollanıyor ve kazanıp kazanmadığı 
    # aşağıda belirlenen ufak bir kural setinde belirleniyor
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # yatay 1
    (bo[4] == le and bo[5] == le and bo[6] == le) or # yatay 2
    (bo[1] == le and bo[2] == le and bo[3] == le) or # yatay 3
    (bo[7] == le and bo[4] == le and bo[1] == le) or # dikey 1
    (bo[8] == le and bo[5] == le and bo[2] == le) or # dikey 2
    (bo[9] == le and bo[6] == le and bo[3] == le) or # dikey 3
    (bo[7] == le and bo[5] == le and bo[3] == le) or # çapraz
    (bo[9] == le and bo[5] == le and bo[1] == le)) # çapraz

def tahtaninKopyasiniAl(tahta):
    # tahtanin scope içinde değişikliğe uğramaması için kopyası alınır
    tahta2 = []

    for i in tahta:
        tahta2.append(i)

    return tahta2

def bosAlanMi(tahta, hamle):
    # Hamle yapılmamış alan ise True döner
    return tahta[hamle].isdigit()


def oyuncununHamlesiniAl(tahta):
    # Oyuncu hamlesini yapar. Oyuncunun oynadığı hamle gerekli kontrollere girer.
    # 1-9 arası bir rakam mı girdi?
    # harf girmemeli
    # oynanmış bir hücreye hamle yapmamalı gibi kontroller
    hamle = ' '
    while hamle not in '1 2 3 4 5 6 7 8 9'.split() or not bosAlanMi(tahta, int(hamle)):
        print('Hamlen? (1-9)')
        hamle = girdi_al()
    return int(hamle)

def tahtadanRandomHamleYap(tahta, hamleListesi):
    # Valid hamle dönülür
    # Eğer oynanabilir hamle yoksa boş dönülür
    olasiHamleler = []
    for i in hamleListesi:
        if bosAlanMi(tahta, i):
            olasiHamleler.append(i)
    #olası hamlelerde random dönüş yapılır
    if len(olasiHamleler) > 0:
        return random.choice(olasiHamleler)
    else:
        return None

def bilgisayarinHamlesiniAl(tahta, bilgisayarinHarfi):
    # Oyuncu Harfi atanır
    if bilgisayarinHarfi == 'X':
        oyuncununHarfi = 'O'
    else:
        oyuncununHarfi = 'X'

    # Basit bir tik tak tok algoritması
    # İlk kontrol eğer sonraki hamlede oyunu kazanabilecekse, hamleyi yapar
    for i in range(1, 10):
        copy = tahtaninKopyasiniAl(tahta)
        if bosAlanMi(copy, i):
            hamleYap(copy, bilgisayarinHarfi, i)
            if kazandimi(copy, bilgisayarinHarfi):
                return i

    # Sonraki kontrol ise oyuncu sonraki hamlede oyunu kazanacaksa onu engeller
    for i in range(1, 10):
        copy = tahtaninKopyasiniAl(tahta)
        if bosAlanMi(copy, i):
            hamleYap(copy, oyuncununHarfi, i)
            if kazandimi(copy, oyuncununHarfi):
                return i

    # Sonrakinde ise köşe almaya çalışır.
    move = tahtadanRandomHamleYap(tahta, [1, 3, 7, 9])
    if move != None:
        return move

    # Merkezi almaya çalışır
    if bosAlanMi(tahta, 5):
        return 5

    # Yan tarafları almaya çalışır
    return tahtadanRandomHamleYap(tahta, [2, 4, 6, 8])

def tahtaDolduMu(tahta):
    for i in range(1, 10):
        if bosAlanMi(tahta, i):
            return False
    return True

def main():
    print('_____Tik Tak Tok Oyunu_____')
    #Rasgele sayı üreten random kütüphanesinde bir değer ürettiğimizde genel olarak bu değer, sistem tarafından üretilen önceki sayıdır.
    #Bununla birlikte, random'u ilk kez kullandığınızda, önceden bir değer yoktur. o yüzden random.seed() çağrılır.
    random.seed()
    while True:
        # Tahta sıfırlanır.
        tahta = [' '] * 10
        for i in range(9,0,-1):
            tahta[i] = str(i)
        oyuncununHarfi, bilgisayarinHarfi = oyuncununHarfiniAl()
        sira = yaziTura()
        print('İlk başlayan : ' + sira )
        oyunOynaniyormu = True
    
        while oyunOynaniyormu:
            if sira == 'oyuncu':
                # Oyuncunun sırası.
                tahtayiCiz(tahta)
                move = oyuncununHamlesiniAl(tahta)
                hamleYap(tahta, oyuncununHarfi, move)
    
                if kazandimi(tahta, oyuncununHarfi):
                    tahtayiCiz(tahta)
                    print('Tebrikler champ. Kazandın!')
                    oyunOynaniyormu = False
                else:
                    if tahtaDolduMu(tahta):
                        tahtayiCiz(tahta)
                        print('Oyun berabere bitti!')
                        break
                    else:
                        sira = 'bilgisayar'
    
            else:
                # Bilgisayarın sırası.
                move = bilgisayarinHamlesiniAl(tahta, bilgisayarinHarfi)
                hamleYap(tahta, bilgisayarinHarfi, move)
    
                if kazandimi(tahta, bilgisayarinHarfi):
                    tahtayiCiz(tahta)
                    print('Bilgisayar seni yendi. Kaybettin :(')
                    oyunOynaniyormu = False
                else:
                    if tahtaDolduMu(tahta):
                        tahtayiCiz(tahta)
                        print('Oyun berabere bitti!')
                        break
                    else:
                        sira = 'oyuncu'
        
        if not yenidenOyna():
            #oyuncu yeniden oynamak istemezse while döngüsünden çıkılır.
            break
        
if __name__ == "__main__":
    main()
