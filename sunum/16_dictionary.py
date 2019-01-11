ltunes_personnels = {}
ltunes_personnels = {
    "Korcan" : 31,
    "Oğuzhan" : 31,
    "Melih" : 27,
    "Küpeli" : 56,
    "Sibel" : 18,
    "Deniz": 34
    }
print("Tüm lTunes üyeleri : {}".format(ltunes_personnels))
print("lTunes üyesi korcan : {}".format(ltunes_personnels["Korcan"]))
ltunes_personnels["Üsame"] = 27
print("Yeni eklenen lTunes üyesi Üsame : {}".format(ltunes_personnels["Üsame"]))
del ltunes_personnels["Deniz"]
print("Tüm lTunes üyeleri : {}".format(ltunes_personnels))

print("Tüm lTunes üyeleri isimleri: {}".format(ltunes_personnels.keys()))
isim_listesi = list(ltunes_personnels.keys())
print("Tüm lTunes üyeleri isimleri: {}".format(isim_listesi))

print("Tüm lTunes üyeleri yaş listesi: {}".format(list(ltunes_personnels.values())))

print("Tüm lTunes üyeleri isim ve yaş listesi: {}".format(list(ltunes_personnels.items())))
