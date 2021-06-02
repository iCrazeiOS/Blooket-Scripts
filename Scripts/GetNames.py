import requests, json, argparse

parser = argparse.ArgumentParser(description="Test")
parser.add_argument("-p", help="Game pin")

args = parser.parse_args()

gamePin = str(args.p)

# Join the game with our fake player
# We use this player to get some info about the game session
r = requests.put("https://api.blooket.com/api/firebase/join", data={
	"id": gamePin,
	"name": "blooketbad"
}, headers={
	"Referer": "https://www.blooket.com/"
})

# Store the data returned from the call of the join endpoint
joinText = r.text

# Send request to kick the custom player
r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name=blooketbad", headers={
	"Referer": "https://www.blooket.com/"
})

if "msg" in json.loads(joinText) and json.loads(joinText)["msg"] == "no game":
	print("No game exists with that pin")
	exit()

jsonInfo = json.loads(joinText)["host"]
if not "c" in jsonInfo:
	print("There are no players in that game")
	exit()
	
playerList = ""
# Get a list of players
for name in jsonInfo["c"].keys():
	playerList += f"{name}\n"
print(playerList)
