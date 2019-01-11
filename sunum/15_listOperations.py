#sadece sayı içeren liste
sampleList = [1,2,3,4,5,6]
#aynı listede sayı, harf ve bool değerler bulunabilir.
sampleList2 = ["A","B","C",1,4,56,True,False]
#liste içinde liste bulunabilir
sampleList2 = [1,[4,5],3,[98,72],5,6]
#listenin sonuna ekleme işlemi append komutu ile yapılır.
sampleList.append(88)
print("append() işleminden sonra\nListe1 :{}".format(sampleList))
#listenin sonundaki elemanı silme işlemi ise pop ile yapılır.
sampleList.pop()
print("pop() işleminden sonra\nListe1 :{}".format(sampleList))
#listede belli bir elemanı çıkarmak için ise pop komutuna parametre olarak elemanın indexi verilebilir
sampleList.pop(1)
print("pop(1) işleminden sonra\nListe1 :{}".format(sampleList))
#liste içindeki elemanların sayısı ise len komutu ile alınır.
print("Liste1 eleman sayısı:{}".format(len(sampleList)))
