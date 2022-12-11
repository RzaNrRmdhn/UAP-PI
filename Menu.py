from SignUp import SignUp
from Theme import Theme
import Login
import os

def Menu():
    os.system('cls')
    Theme.themeTODO()
    try:
        menu = [
            "Selamat Datang",
            "1. Sign Up",
            "2. Login",
            "3. Exit"
        ]

        for i in range(4):
            print(menu[i])

        Pilihan = int(input('Masukkan Pilihan: '))

        if(Pilihan == 1):
            SignUp()

        elif(Pilihan == 2):
            os.system('cls')
            Theme.themeLogin()
            nama = str(input('Masukkan Nama: '))
            npm = int(input('Masukkan Pass: '))
            Login.Login(nama=nama, npm=npm)

        else:
            print('Thank You!')
            
    except:
        os.system('cls')
        Menu()