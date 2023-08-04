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
        uuid = self.playernametouuid("ColonLLC")
        api_url = f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}"
        print(api_url)
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
        return (
            data["player"]["stats"]["Duels"].get("bridge_duel_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_2v2v2v2_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_3v3v3v3_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_doubles_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_threes_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_four_losses", 0)
        )
    def GetBridgeWinLossRatio(self,username):
        if self.ValidApiToken == False:
            raise Exception("Invalid API Token")
        uuid = self.playernametouuid(username)
        hypixelURL = f"https://api.hypixel.net/player?key={self.api_key}&uuid={uuid}"
        response = requests.get(hypixelURL)
        data = response.json()
        if data["success"] == False:
            raise Exception("Bad Username")
        losses = (
            data["player"]["stats"]["Duels"].get("bridge_duel_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_2v2v2v2_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_3v3v3v3_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_doubles_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_threes_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_four_losses", 0)
        )
        wins = data["player"]["achievements"].get("duels_bridge_wins", 0)
        if wins == 0:
            return 0
        if losses == 0:
            return wins
        return round(wins/losses * 10 ) / 10
    def GetKillDeathRatio(self,username):
        if self.ValidApiToken == False:
            raise Exception("Invalid API Token")
        uuid = self.playernametouuid(username)
        hypixelURL = f"https://api.hypixel.net/player?key={self.api_key}&uuid={uuid}"
        response = requests.get(hypixelURL)
        data = response.json()
        if data["success"] == False:
            raise Exception("Bad Username")
        deaths = data["player"]["stats"]["Duels"].get("bridge_deaths", 0)
        kills = data["player"]["stats"]["Duels"].get("bridge_kills", 0)
        if kills == 0:
            return 0
        elif deaths == 0:
            return kills
        return kills/deaths
    def GetBridgeInfo(self,username):
        if self.ValidApiToken == False:
            raise Exception("Invalid API Token")
        uuid = self.playernametouuid(username)
        hypixelURL = f"https://api.hypixel.net/player?key={self.api_key}&uuid={uuid}"
        response = requests.get(hypixelURL)
        data = response.json()
        if data["success"] == False:
            raise Exception("Bad Username")
        losses = (
            data["player"]["stats"]["Duels"].get("bridge_duel_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_2v2v2v2_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_3v3v3v3_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_doubles_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_threes_losses", 0)
            + data["player"]["stats"]["Duels"].get("bridge_four_losses", 0)
        )
        wins = data["player"]["achievements"].get("duels_bridge_wins", 0)
        if wins == 0:
            winloss = 0
        elif losses == 0:
            winloss = wins
        else:
            winloss = round(wins/losses * 10 ) / 10
        deaths = data["player"]["stats"]["Duels"].get("bridge_deaths", 0)
        kills = data["player"]["stats"]["Duels"].get("bridge_kills", 0)
        if kills == 0:
            kdr = 0
        elif deaths == 0:
            kdr = kills
        else:
            kdr = kills/losses
        return [wins,losses,winloss,kdr]
if __name__ == "__main__":
    with open (".apikey.txt","r") as file:
        apikey = file.read()
    bs = GetBridgeData(apikey)
    winloss = bs.GetBridgeWinLossRatio("ColonLLC")
    print("winloss of ColonLLC", winloss)