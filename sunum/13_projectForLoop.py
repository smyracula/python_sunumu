n=int(input("Kaç satır olsun?\n"))
for i in range (n,0,-1):
    print((n-i) * ' ' + i * '| ')
