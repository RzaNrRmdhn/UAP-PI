from Theme import Theme
from API_KEY import Token
import UpdatePage
import createPages
import Catatan
import openWeb
import os

def Home(nama):
    Theme.themeTODO()
    home = [
        "Welcome %s" %nama,
        "Buat Catatan ataupun toDo list",
        "1. Create todo list/Catatan Online",
        "2. Create todo list/Catatan Offline(Local)",
        "3. Update todo List",
        "4. Cek Catatan Online",
    ]

    for i in range(6):
        print(home[i])

    try:
        pilih = int(input('Masukkan Pilihan: '))

        if (pilih == 1):
            os.system('cls')
            createPages.createPages(Token.databaseId, Token.headers, nama)
        elif (pilih == 2):
            os.system('cls')
            Catatan.Noted(nama)
        elif (pilih == 3):
            os.system('cls')
            UpdatePage.pageId(nama)
        elif (pilih == 4):
            os.system('cls')
            openWeb.Web(nama)
    except:
        os.system('cls')
        Home(nama)