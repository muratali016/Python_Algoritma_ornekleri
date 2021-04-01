import random
sorular={"adınız":"murat","yaşınız":"genç","meslek":"öğrenci"}

print( random.choice(list(sorular.keys())))

sorusayısı=len(sorular)

while sorusayısı>1:
    soru=random.choice(list(sorular.keys()))
    print(soru)
    cevap=input(soru)
    dogrucevap=sorular[soru]
    if cevap == dogrucevap:
        sorular.pop(soru)
        print ("tebrikler")
        
    else:
            print("yanlış cevap doğrusu",dogrucevap)
            
print("tebrikler")            
            
    