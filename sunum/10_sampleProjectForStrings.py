# nonstring karakterler
nonstrings = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "ITUNES!!!, Üsame ---candır."

# Kullanıcıdan Girdi için
# my_str = input("Bir cümle gir: ")

# girilen stringten nonstring karakterler kaldırılır
clean_string = ""
for char in my_str:
   if char not in nonstrings:
       clean_string = clean_string + char

# son hali
print(clean_string)
