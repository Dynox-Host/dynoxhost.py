import requests
class dynoxhost:
    def __init__(self, token):
        try:
            token
        except NameError:
            print("Api token was not provided")
        self.token = token
    
    def getUsage(self, id):
        try:
            id
        except NameError:
            print("Server id was not provided")
        res = requests.get(f"https://panel.dynoxhost.tk/api/client/servers/${id}/resources", headers={ 'Authorization': f"Bearer ${self.token}", 'Content-Type': 'application/json', 'Accept': 'application/json' })
        if res.status_code == 404:
            NameError("Invalid server id")
        return res.json()