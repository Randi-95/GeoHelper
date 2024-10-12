print('\n   ======================================')
print('   || SELAMAT DATANG DI GEOMATH HELPER ||')
print('   ======================================')

def luas_persegi():
    print("------------")
    print('LUAS PERSEGI')
    print("------------")
    sisi = float (input ("masukkan sisi: "))
    hasil = sisi*sisi
    print('============================================')
    print('hasil dari luas persegi: ', hasil, )
    print('============================================')



def keliling_persegi():
    print("----------------")
    print("KELILING PERSEGI")
    print("----------------")
    sisi = float (input ('masukkan sisi: '))
    hasil = 4*sisi
    print('============================================')
    print("hasil keliling persegi: ", hasil, )
    print('============================================')


def luas_persegipanjang():
    print("--------------------")
    print("LUAS PERSEGI PANJANG")
    print("--------------------")
    panjang = float (input ('masukkan panjang: '))
    lebar = float (input ('masukkan lebar: '))
    hasil = panjang*lebar
    print('============================================')
    print("hasil keliling persegi panjang: ", hasil, )
    print('============================================')


def keliling_persegipanjang():
    print("------------------------")
    print("KELILING PERSEGI PANJANG")
    print("------------------------")
    panjang = float (input ('masukkan panjang: '))
    lebar = float (input ('masukkan lebar: '))
    hasil = 2 * (panjang + lebar)
    print('============================================')
    print("hasil luas persegi panjang: ", hasil, )
    print('============================================')


def luas_segitiga():
    print("-----------------------")
    print("LUAS SEGITIGA SEMBARANG")
    print("-----------------------")
    tinggi = float (input ('masukkan tinggi: '))
    alas = float (input ('masukkan alas: '))
    hasil = 0.5 * alas * tinggi
    print('============================================')
    print("hasil luas segitiga sembarang: ", hasil, )
    print('============================================')


def keliling_segitiga():
    print("---------------------------")
    print("KELILING SEGITIGA SEMBARANG")
    print("---------------------------")
    sisi1 = float (input ('masukkan sisi 1: '))
    sisi2 = float (input ('masukkan sisi 2: '))
    sisi3 = float (input ('masukkan sisi 3: '))
    hasil = sisi1 + sisi2 + sisi3
    print('============================================')
    print("hasil keliling segitiga sembarang: ", hasil, )
    print('============================================')

def luas_trapesium():
    print("--------------")
    print("LUAS TRAPESIUM")
    print("--------------")
    sisia = float (input ('masukkan sisi atas: '))
    sisib = float (input ('masukkan sisi bawah: '))
    tinggi = float (input ('masukkan tinggi: '))
    hasil = 0.5 * (sisia + sisib) * tinggi 
    print('============================================')
    print("hasil luas trapesium: ", hasil, )
    print('============================================')

def keliling_trapesium():
    print("------------------")
    print("KELILING TRAPESIUM")
    print("------------------")
    sisiatas = float (input ('masukkan sisi atas: '))
    sisibawah = float (input ('masukkan sisi bawah: '))
    sisimiring1 = float (input ('masukkan sisi miring 1: '))
    sisimiring2 = float (input ('masukkan masukkkan sisi miring 2: '))
    hasil = sisiatas + sisibawah + sisimiring1 + sisimiring2
    print('============================================')
    print("hasil keliling trapesium: ", hasil, )
    print('============================================')

def luas_lingkaran():
    print("--------------")
    print("LUAS LINGKARAN")
    print("--------------")
    jari_jari = float (input ('masukkan jari-jari lingkaran: '))
    hasil = 3.14 * jari_jari**2
    print('============================================')
    print("hasil luas keliling: ", hasil, )
    print('============================================')

def keliling_lingkaran():
    print("--------------")
    print("KELILING LINGKARAN")
    print("--------------")
    jari_jari = float (input ('masukkan jari-jari lingkaran: '))
    hasil = 2 * 3.14 * jari_jari
    print('============================================')
    print("hasil keliling lingkaran: ", hasil, )
    print('============================================')

def volume_balok():
    print("------------")
    print("VOLUME BALOK")
    print("------------")
    panjang = float (input ('masukkan panjang: '))
    lebar = float (input ('masukkan lebar: '))
    tinggi = float (input ('masukkan tinggi: '))
    hasil = panjang * lebar * tinggi
    print('============================================')
    print("hasil volume balok: ", hasil, )
    print('============================================')

def keliling_balok():
    print("--------------")
    print("KELILING BALOK")
    print("--------------")
    panjang = float (input ('masukkan panjang: '))
    lebar = float (input ('masukkan lebar: '))
    tinggi = float (input ('masukkan tinggi: '))
    hasil = 4 * (panjang + lebar + tinggi)
    print('============================================')
    print("hasil keliling balok: ", hasil, )
    print('============================================')

def volume_kubus():
    print("------------")
    print("VOLUME KUBUS")
    print("------------")
    sisi = float (input ('masukkan sisi: '))
    hasil = sisi**3
    print('============================================')
    print("hasil volume kubus: ", hasil, )
    print('============================================')

def volume_tabung():
    print("-------------")
    print("VOLUME TABUNG")
    print("-------------")
    jari_jari = float (input ('masukkan jari: '))
    tinggi = float (input ('masukkan tinggi: '))
    hasil = 3.14 * jari_jari**2 * tinggi
    print('============================================')
    print("hasil volume tabung: ", hasil, )
    print('============================================')

def volume_kerucut():
    print("--------------")
    print("VOLUME KERECUT")
    print("--------------")
    jari_jari = float (input ('masukkan jari jari: '))
    tinggi = float (input ('masukkan tinggi: '))
    hasil = 1/3 * 3.14 * jari_jari**2 * tinggi
    print('============================================')
    print("hasil volume kerucut: ", hasil, )
    print('============================================')


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" SILAHKAN PILIH RUMUS YANG AKAN ANDA GUNAKAN")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    userInput = int(input ("PILIH RUMUS BANGUN RUANG: \n1.Luas Persegi \n2.Keliling Persegi \n3.Luas Persegi Panjang \n4.Keliliing Persegi Panjang\n5.Luas Segitiga Sembarang\n6.Keliling Segitiga Sembarang\n7.Luas Trapesium\n8.Keliling Trapesium\n9.Luas Lingkaran\n10.Keliling Lingkaran\n\nPILIH RUMUS BANGUN RUANG: \n11.Volume Balok\n12.Keliling Balok\n13.Volume Kubus\n14.Volume Tabung\n15.Volume Kerucut\n0.Keluar\n============================================= \n \nPILIH NOMOR BERAPA: "))
    if (userInput  == 1):
        luas_persegi()

    elif (userInput ==2):
        keliling_persegi()

    elif (userInput ==3):
        luas_persegipanjang()

    elif (userInput ==4):
        keliling_persegipanjang()

    elif (userInput ==5):
        luas_segitiga()

    elif (userInput ==6):
        keliling_segitiga()

    elif (userInput ==7):
        luas_trapesium()
    
    elif (userInput ==8):
        keliling_trapesium()

    elif (userInput ==9):
        luas_lingkaran()

    elif (userInput ==10):
        keliling_lingkaran()

    elif (userInput ==11):
        volume_balok()

    elif (userInput ==12):
        keliling_balok()
    
    elif (userInput ==13):
        volume_kubus()

    elif (userInput ==14):
        volume_tabung()

    elif (userInput ==15):
        volume_kerucut()

    elif (userInput ==0):
       break






