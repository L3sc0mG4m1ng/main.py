import random
karakter =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

cevap = int(input("parolanızın kaç karakter olmasını istersiniz?"))

sayim = ""

for i in range(cevap):
    sayim = sayim + random.choice(karakter)
    
    
print(sayim)
