import requests
class GetBridgeData:
    def playernametouuid(self,playername):
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{playername}")
        data = response.json()
        if "errorMessage" in data:
            raise Exception("Invalid username")
        else:
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
            print("you called this method", data["player"]["achievements"]["duels_bridge_wins"])
            return data["player"]["achievements"]["duels_bridge_wins"]
    def GetBridgeLosses(self,username):
        if self.ValidApiToken == False:
            raise Exception("Invalid API Token")
        uuid = self.playernametouuid(username)
        hypixelURL = f"https://api.hypixel.net/player?key={self.api_key}&uuid={uuid}"
        response = requests.get(hypixelURL)
        data = response.json()
        if data["success"] == False:
            raise Exception("Bad Username")
        else:
            print("you called this method", data["player"]["achievements"]["duels_bridge_wins"])
            return data["player"]["stats"]["Duels"]["bridge_duel_losses"]
if __name__ == "__main__":
    with open (".apikey.txt","r") as file:
        apikey = file.read()
    bs = GetBridgeData(apikey)
    wins = bs.GetBridgeWins("ColonLLC")
    losses = bs.GetBridgeLosses("ColonLLC")
    print("winloss of ColonLLC", wins/losses)