from API_KEY import Token
import requests, json, os, time, Theme, HomeScreen

def pageId(nama):
    count = 1
    url = "https://api.notion.com/v1/search"
    payload = {"page_size": 100}

    response = requests.post(url, headers=Token.headers)
    data = response.json()['results']
    print("Daftar Id: ")
    print("NOTE: 2 Id terakhir id database")
    for i in data:
        # if(count <= 3):
        print("%d." %count, i['id'])
        count = count + 1

    id = input("Ketik Id: ")
    if(len(id) > 0):
        UpdatePage(nama, id)
    else:
        os.system('cls')
        HomeScreen.Home(nama)
    

def UpdatePage(nama, id):
    Theme.Theme.themeList()
    Title = input('Masukkan Title todo: ')
    Status = input('Masukkan Status(On going atau Done): ')
    Link = input('Masukkan Link File(Optional): ')

    Status = Status.upper()
    Check = bool(Status == "DONE")
    if(len(Link) == 0):
        Link = ' '

    if(len(Title) == 0 or len(Status) == 0):
        print('Title atau Status tidak boleh kosong!')
        time.sleep(3)
        os.system('cls')
        UpdatePage(nama, id)

    updateUrl = f"https://api.notion.com/v1/pages/{id}"
    updateData = {
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
    data = json.dumps(updateData)
    response = requests.request("PATCH", updateUrl, headers=Token.headers, data=data)
    print(response.status_code)
    print(response.text)
    time.sleep(3)
    os.system('cls')
    HomeScreen.Home(nama=nama)
