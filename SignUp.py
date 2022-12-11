from daftarAkun import akun
from time import sleep
from HomeScreen import Home
from Theme import Theme
import os

def SignUp():
    Theme.themeSignUp()
    try:
        nama = str(input('Masukkan Username: '))
        Npm = int(input('Masukkan Password: '))

        if (nama != nama.upper()):
            os.system('cls')
            print('Username harus dalam UPPER CASE!')
            sleep(3)
            os.system('cls')
            SignUp()
        else:
            akun.append({"Username":nama, "Npm":Npm})
            os.system('cls')
            Home(nama=nama)
    except:
        os.system('cls')
        SignUp