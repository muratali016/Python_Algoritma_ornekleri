import random
liste_sayisi = 1
liste_icerik_sayisi = random.randint(5,10)
listeler = list()

for i in range(liste_sayisi):
    liste = list()
    for e in range(liste_icerik_sayisi):
        liste.append(random.randint(1, 10))
    listeler.append(liste)
    
print(listeler) 
print(liste)

eleman1= random.choice(liste)
eleman2=random.choice(liste)
   
rastgele_seçilenler=[]
rastgele_seçilenler.append(eleman1)
rastgele_seçilenler.append(eleman2)
print(rastgele_seçilenler)

toplam =eleman1+eleman2 #rastgelelrin toplamı



girdi=int(input("eleman giriniz: ")) # alınan ifade



while toplam!=0  :
    
    
    if toplam==girdi:
        print("girdiğiniz sayı rastgele listedeki iki lemanın toplamına eşittir.")
        break
    elif toplam!=girdi:
        eleman1= random.choice(liste)
        eleman2=random.choice(liste)
        
        toplam=eleman1+eleman2
        print (toplam)  

