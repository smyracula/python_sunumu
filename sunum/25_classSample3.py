#Encapsulation
class Team:
        def __init__(self):
                self.isim = takimIsmi
                self.sayi = uyeSayisi
        def bilgi(self):
                print("Doğuş Teknoloji'de yer alan {} takımı {} kişiden oluşur.".format(self.isim,self.sayi))
        def takimTuru(self):
                print("ne idüğü belirsiz")
        def setIsim(self,isim):
                self.isim = isim
        def getIsim(self):
                return self.isim
        def setSayi(self,sayi):
                self.sayi = sayi
        def getSayi(self):
                return self.sayi
        
class KanbanTeam(Team):
        def __init__(self,takimIsmi,uyeSayisi):
                self.isim = takimIsmi
                self.sayi = uyeSayisi
        def bilgi(self):
                print("Kanban!!!  {} ismimiz {} kişiyiz.".format(self.isim,self.sayi))
        def takimTuru(self):
                print("Biz Kanban takımıyız")
kanbanTeam = KanbanTeam("lTunes",18)
kanbanTeam.bilgi()
kanbanTeam.takimTuru()
print("___________________________________")
takimSayisi = kanbanTeam.getSayi()
print("1 kişi işten ayrıldı")
takimSayisi = takimSayisi - 1
kanbanTeam.setSayi(takimSayisi)
kanbanTeam.bilgi()
