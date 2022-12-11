import time, os
import HomeScreen

def Noted(nama):
    Note = input("Nama File: ")
    Kegiatan = input("Input Data: ")


    Catatan = open("%s.txt" %Note, "a")
    Catatan.write("Author: %s" %nama)
    Catatan.write("Todo: %s" %Kegiatan)
    Catatan.close()
    print("Catatan Berhasil dibuat!")
    time.sleep(3)
    os.system('cls')
    HomeScreen.Home(nama=nama)
