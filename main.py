resps = {
    "oi": "Oi :3",
    "olá": "Oi :3",
    "ola": "Oi :3",
    "salve": "Oi :3",
    "eae": "Oi :3",
    "oscar": "Oscar!? Esse nome eh familiar, ok isso foi bem avulso...",
    "você é legal": "vlw <3",
    "você eh legal": "vlw <3",
    "voce é legal": "vlw <3",
    "voce eh legal": "vlw <3",
    "vc é legal": "vlw <3",
    "vc eh legal": "vlw <3",
}

while True:
    user = input('\nVocê: ').lower()
    try: 
        if resps[user]:
            print('\nMei: ' + resps[user])
    except:
        continue