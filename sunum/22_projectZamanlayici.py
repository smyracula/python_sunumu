import time

print('başlamak için -> ENTER\nbitirmek için -> Ctrl + C')
while True:
    try:
        input()
        baslangic = time.time()
        print('Başladı',baslangic)
    except KeyboardInterrupt:
        bitis = time.time()
        print('Bitti',bitis)
        print('Geçen Zaman:', round(bitis - baslangic,2),' saniye')
        break
        
