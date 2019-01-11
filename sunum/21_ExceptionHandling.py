def hataFirlat(i):
    #bu condition true ise program devam eder ve except içine düşmez.
    assert(i!=1),"Değer 1 olmamalı. Gönderilen Değer:{}".format(i)
    print("Değer 1 değildir")


try:
    print("2")
    hataFirlat(2)
    print("3")
    hataFirlat(3)
except AssertionError:
    print("Hata:{}".format(AssertionError))

try:
    print("1")
    hataFirlat(1)
except AssertionError:
    print("Bu hata sonucu buraya düştü.")


try:
    raise Exception('Bu hata aldığında program durmaz.')
    raise ValueError('Bu hata aldığında program patlar')
except Exception as error:
     print('Hata: ' + repr(error))

        
#Aşağıdaki satırda try bloğunda olmadığı için program patlayacak    
#hataFirlat(1)
