karakterler ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("lütfen oluşturmak istediğiniz parolanın uzunluğunu giriniz"))

parola = ""

import random
for i in range(parola_uzunlugu):
    parola += random.choice(karakterler)

print(parola)    
