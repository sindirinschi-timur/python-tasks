import requests

def chuck_norris():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data['value'])
    else:
        print("Try again.")

chuck_norris()