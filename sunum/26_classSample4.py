#Polymorphism : Çokbiçimlilik, bir nesnenin farklı amaçlar için de kullanılabileceği anlamına gelir 
class Team:
        def __init__(self):
                self.isim = takimIsmi
                self.sayi = uyeSayisi
        def bilgi(self):
                print("Doğuş Teknoloji'de yer alan {} takımı {} kişiden oluşur.".format(self.isim,self.sayi))
        def takimTuru(self):
                print("ne idüğü belirsiz")
        
class ScrumTeam(Team):
        def __init__(self,takimIsmi,uyeSayisi):
                self.isim = takimIsmi
                self.sayi = uyeSayisi
        def takimTuru(self):
                print("Biz Scrum takımıyız")

class KanbanTeam(Team):
        def __init__(self,takimIsmi,uyeSayisi):
                self.isim = takimIsmi
                self.sayi = uyeSayisi
        def bilgi(self):
                print("Kanban!!!  {} ismimiz {} kişiyiz.".format(self.isim,self.sayi))
        def takimTuru(self):
                print("Biz Kanban takımıyız")

class OtherTeam(Team):
        def __init__(self,takimIsmi,uyeSayisi):
                self.isim = takimIsmi
                self.sayi = uyeSayisi
        def bilgi(self):
                print("{} olarak {} kişilik ekibimiz emrininizdedir.".format(self.isim,self.sayi))


def bilgiYazdir(team):
        team.bilgi()
        
scrumTeam = ScrumTeam("Marvel",8)
bilgiYazdir(scrumTeam)
scrumTeam.takimTuru()

kanbanTeam = KanbanTeam("lTunes",18)
bilgiYazdir(kanbanTeam)
kanbanTeam.takimTuru()

otherTeam = OtherTeam("Ameleler",2)
bilgiYazdir(otherTeam)
otherTeam.takimTuru()
