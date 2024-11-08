import sys



def kali(x, y) :
      return  x * y

def bagi(x, y) :
      return x / y

def jumlah(x, y) :
       return x + y
    
def kurang(x, y) :
       return x - y
       
def pangkat(x, y) :
	return x ** y
print("""

====>MAU PILIH APA<====
  [==Yg Buat Elek==]
 1] Penjumlahan
 2] Pengurangan
 3] Perkalian
 4] Pembagian
 5] Pangkat
 6] Tampilkan Semua
 
""" )

try :
	              pilihan = int(input("[•] Masukan Pilihan Mu : "))
except ValueError :
	              print("[-_-] Pilih Yang Bener Kocak!!")
	              sys.exit()
	
if pilihan == 1 :
	 angka1 = int(input("[•] Masukan angka pertama : "))
	 angka2 = int(input("[•] Masukan angka kedua : "))
	 print(f"[•]Hasil Penjumlahan = {jumlah(angka1, angka2)}")
	 
elif pilihan == 2 :
	angka1 = int(input("[•] Masukan angka pertama : "))
	angka2 = int(input("[•] Masukan angka kedua : "))
	print(f"[•] Hasil Pengurangan = {kurang(angka1, angka2)}")
	
elif pilihan == 3 :
     angka1 = float(input("[•] Masukan angka pertama : "))
     angka2 = float(input("[•] Masukan angka kedua : "))
     print(f"[•] Hasil Perkalian = {kali(angka1, angka2)}")
    
elif pilihan == 4 :
      angka1 = float(input("[•] Masukan angka pertama : "))
      angka2 = float(input("[•] Masukan angka kedua : "))
      print(f"[•] Hasil Pembagian = {bagi(angka1, angka2)}")
      
elif pilihan == 5 :
      angka1 = int(input("[•] Masukan angka pertama : "))
      angka2 = int(input("[•] Masukan angka kedua : "))
      print(f"Hasil Pangkat = {pangkat(angka1, angka2)}")
      
elif pilihan == 6 :
       angka1 = float(input("[•] Masukan angka pertama : "))
       angka2 = float(input("[•] Masukan angka kedua : "))
       print(f"[•] Hasil Penjumlahan = {jumlah(angka1, angka2)}")
       print(f"[•] Hasil Pengurangan = {kurang(angka1, angka2)}")
       print(f"[•] Hasil Perkalian = {kali(angka1, angka2)}")
       print(f"[•] Hasil Pembagian = {bagi(angka1, angka2)}")
       print(f"[•] Hasil Pangkat = {pangkat(angka1, angka2)}")
       
else :
	print("[•] Pilih Apa coba -_-")