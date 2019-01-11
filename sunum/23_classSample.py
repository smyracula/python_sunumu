class ScrumTeam:
        def __init__(self,takimIsmi,uyeSayisi):
                self.isim = takimIsmi
                self.sayi = uyeSayisi
        def bilgi(self):
                print("Doğuş Teknoloji'de yer alan {} takımı {} kişiden oluşur.".format(self.isim,self.sayi))

scrumTeam = ScrumTeam("lTunes",19)
scrumTeam.bilgi()
                
