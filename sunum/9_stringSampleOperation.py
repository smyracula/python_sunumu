#Girilen text için harflardeki kelimeleri, Kelime Sayılarını bulan çözüm
wordstring = input("giris yap ")
wordlist = wordstring.split()
wordfreq = [wordlist.count(w) for w in wordlist]

print("Girilen text\n {} \n".format(wordstring))

print("Kelime Listesi\n {} \n".format(str(wordlist)))

print("Kelime Sayıları\n {} \n".format(str(wordfreq)))

print("Kelime Sayıları Karşılıkları\n {} \n".format(dict(zip(wordlist,wordfreq))))
