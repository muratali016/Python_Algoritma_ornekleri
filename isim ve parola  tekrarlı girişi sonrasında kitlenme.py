bilgiler=("murat","murat123")

isim=input("isminizi girin ")

parola=input("parolayı girin ")

hata=3

while bilgiler[0] !=isim or bilgiler[1] !=parola:
    hata=hata-1 
    if hata<4 and hata!=0: 
       
       print("şu kadar hakkınız kaldı:",hata)
       
       isim=input("isminizi girin ")
       parola=input("parolayı girin ")
       print("hoşgeldiniz")
    else :
        print("çok fazla deneme yaptınız kilitlendi")
        break



