#Integer (int): Tam sayıları ifade eder. Örneğin, 5, -3, 0 gibi.
x = 10
y = -5

#Float: Ondalıklı sayıları ifade eder. Örneğin, 3.14, 0.5, -2.75 gibi.
x = 3.14
y = -2.5

#Boolean: Sadece iki değer alabilen bir veri tipidir. True (doğru) veya False (yanlış) değerlerini alır.
x = True
y = False

#String: Karakter dizilerini ifade eder. Örneğin, "Merhaba Dünya", "Python Programlama Dili" gibi.
x = "Merhaba Dünya"
y = "Python Programlama Dili"

#List: Birden fazla veriyi bir arada tutmak için kullanılır. Liste, değiştirilebilir bir veri tipidir.
x = [1, 2, 3, 4, 5]
y = ["elma", "armut", "çilek"]

#Tuple: Listelere benzer, ancak değiştirilemez bir veri tipidir.
x = (1, 2, 3, 4, 5)
y = ("elma", "armut", "çilek")

#Set: Benzersiz elemanlardan oluşan bir veri yapısıdır. Sırasız bir yapıya sahiptir.
x = {1, 2, 3, 4, 5}
y = {"elma", "armut", "çilek"}

#Dictionary: Anahtar-değer çiftleri ile tanımlanan bir veri yapısıdır.
x = {"ad": "Ali", "soyad": "Yılmaz", "yaş": 30}
y = {"ürün": "Laptop", "fiyat": 5000}


#SORU 2 -> 

"""
Kullanıcı adı: Bu bir string (metin) veri tipidir. Örnek bir kullanıcı adı: "kocamuli"

Şifre: Bu da bir string (metin) veri tipidir. Örnek bir şifre: "my_password123"

Yaş: Bu bir integer (tam sayı) veri tipidir. Örnek bir yaş: 23

E-posta adresi: Bu yine bir string (metin) veri tipidir. Örnek bir e-posta adresi: "mulisekoca@gmail.com"

İsim ve soyisim: Her ikisi de string (metin) veri tipleridir. Örnek bir isim: "Mulise" ve soyisim: "Koca"


"""

#SORU 3 ->
"""
Giriş kısmındaki şifre if else doğruysa girer yanlışsa tekrar deneyin uyarısı verin.
ödev kısımlarında ya da sayfaların sonundaki Bitir ve Devam et sseçeneğinin tıklanması

"""

username = "muli"
password = "deneme123"

if username == "muli" and password == "deneme123":
    print("Giriş başarılı.")
elif username != "muli":
    print("Kullanıcı adı hatalı.")
else:
    print("Parola hatalı.")


