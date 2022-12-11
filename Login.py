from daftarAkun import akun
import HomeScreen
import Menu
import os
import time

def Login(nama, npm):
    for cek in range(len(akun)):
        if(nama == akun[cek]['Username'] and npm == akun[cek]['NPM']):
            os.system('cls')
            print('Anda Berhasil Login!')
            time.sleep(3)
            os.system('cls')
            HomeScreen.Home(nama=nama)

    else:
        os.system('cls')
        print('404, Gagal Login! Username atau Pass tidak cocok')
        time.sleep(3)
        os.system('cls')
        Menu.Menu()