#tekrar eden elemanlar harici listenin eşit olup olmadığına bakar
A = {1,2,3}
B= {2,3,2,1}
print(A==B)
input("Devam için bir enter \nher bir elemanı dolaşan bir foreach döngüsü")
for v in B:
    print(v)
input("Devam için bir enter \nliste içinde bir değerin var olup olmadığı")

if(1 in B):
    print("B listesi içinde 1 var")
    B.discard(1)
else:
    print("B listesi içinde 1 yok")

input("Devam için bir enter")
if(1 in B):
    print("B listesi içinde 1 var")
else:
    print("B listesi içinde 1 yok")

input("Devam için bir enter")
if(12 not in A):
    print("A listesi içinde 12 yok")
    A.add(12)
else:
    print("A listesi içinde 12 var")
input("Devam için bir enter")
if(12 not in A):
    print("A listesi içinde 12 yok")
else:
    print("A listesi içinde 12 var")
input("Devam için bir enter\nliste içinden bir elemanı silerken remove komutunu kullanacaksanız\nliste içinde mutlaka o değer bulunmalıdır. yoksa hata verir.")
A.remove(9)
