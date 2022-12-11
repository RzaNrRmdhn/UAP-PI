import webbrowser
import HomeScreen
import os  

def Web(nama):
    next = input('Masukkan Pilihan y/n: ')

    next = next.lower()
    if(next == 'y'):
        url = 'https://www.notion.so/7d65f30db93047a2a8ebb6002eef1f25'
        webbrowser.open_new_tab(url)
        Back(nama=nama)
    else:
        HomeScreen.Home(nama=nama)



def Back(nama):
    os.system("PAUSE")
    os.system('cls')
    HomeScreen.Home(nama=nama)
