from Theme import Theme
import requests
import json
import time
import os
import HomeScreen

def createPages(databaseID, headers, nama):
    Theme.themeList()
    Title = input('Masukkan Title todo: ')
    Status = input('Masukkan Status(On Going atau Done): ')
    Link = input('Masukkan Link File(Optional): ')

    Status = Status.upper()
    Check = bool(Status == "DONE")
    if(len(Link) == 0):
        Link = ' '

    if(len(Title) == 0 or len(Status) == 0):
        print('Title atau Status tidak boleh kosong!')
        time.sleep(3)
        os.system('cls')
        createPages(databaseID=databaseID, headers=headers, nama=nama)

    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": { "database_id": databaseID },
        "properties": {
            "Kegiatan": {
                "title": [
                    {
                        "text": {
                            "content": "%s" %Title
                        }
                    }
                ]
            },
            "Nama": {
                "rich_text": [
                    {
                        "text": {
                            "content": "%s" %nama
                        },
                    }
                ]
            },
            "Checkbox": {
                "checkbox": Check
            },
            "Select": {
                "select": {
                    "name": "%s" %Status
                } 
            },
            "Link": {
                "url": "%s" %Link
            }
        }
    }
    data = json.dumps(newPageData)
    res = requests.post(createUrl, headers=headers, data=data)
    print(res.status_code)
    print(res.text)
    time.sleep(3)
    os.system('cls')
    HomeScreen.Home(nama=nama)