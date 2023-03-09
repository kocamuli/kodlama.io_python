print("Kodlama.io")

#değişken tanımlama : bir tip belirtecine ihtiyaç duyulmaz. 
baslik = "TAŞIT KREDİSİ"
print(baslik)

#int : tam sayı
vade = 36
vade2 = "36"
#vade ile vade2 arasındaki fark -> vade numeric bir ifadedir 
#vade2 ise metinsel bir ifadedir
#print(vade+vade2) -> HATA VERİR. ÇÜNKÜ str+int TOPLANAMAZ.

#float,double,decimal
aylikOdeme = 200.50 #float türündedir.
print(vade+aylikOdeme)

#bool -> 1 ve o'lardan oluşur.
yukselisteMi = True
alcalistaMi = False

#matematikselOperatörler :
print(5+2)
print(30-5)
print(5*105)
print(vade*aylikOdeme)
print(152/2)
print(105%2)

#mantıksal operatörler
print(1==1)
print(3>2)
print(55>=55)
print(3<2)

print(1>2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2) #TRUE GELİR ->TRUE AND TRUE -> SOLDAN BAŞLAR OKUMAYA

#karar yapıları :
#if elif else 

sayi1 =10
sayi2 =15

#sayi1 > sayi2 ise BÜYÜKTÜR YAZ

if(sayi1>sayi2):
    print(sayi1 , "BÜYÜKTÜR" , sayi2 , "'DEN")
elif(sayi1<sayi2):
    print(sayi2 , "BÜYÜKTÜR" , sayi1 , "'dan")

