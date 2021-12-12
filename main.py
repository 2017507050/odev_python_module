import modüll
print (modüll.sene)
print(modüll.msj)

sayı1=int(input("1.sayıyı giriniz: "))
sayı2=int(input("2.sayıyı giriniz: "))

a=modüll.topla(sayı1,sayı2)
print("2 sayının toplamı=",a)

b=modüll.çıkar(sayı1,sayı2)
print("2 sayının farkı=",b)

c=modüll.çarp(sayı1,sayı2)
print("2 sayının çarpımı=",c)

d=modüll.bölme(sayı1,sayı2)
print("2 sayının bölümü=",d)