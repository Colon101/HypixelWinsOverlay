import requests
class GetBridgeWinsData:
    def playernametouuid(self,playername):
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{playername}")
        data = response.json()
        print("uuid:",data["id"])
        return data["id"]
    def __init__(self,api_key):
        #Checking if api key is valid
        self.api_key = api_key
        uuid = self.playernametouuid("Hypixel")
        api_url = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"
        response = requests.get(api_url)
        data = response.json()
        if data["success"] == False:
            self.ValidApiToken = False
        else:
            self.ValidApiToken = True
    def GetBridgeWins(self,username):
        if self.ValidApiToken == False:
            raise Exception("Invalid API Token")
        uuid = self.playernametouuid(username)
        hypixelURL = f"https://api.hypixel.net/player?key={self.api_key}&uuid={uuid}"
        response = requests.get(hypixelURL)
        data = response.json()
        if data["success"] == False:
            raise Exception("Bad Username")
        else:
            return 
if __name__ == "__main__":
    bs = GetBridgeWinsData("7b02024f-8f7a-479d-ae5a-f4d3def54d08")