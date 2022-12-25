class Token:
    token = '' # Use Your Token

    databaseId = '' # Use Your DatabaseId

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }
