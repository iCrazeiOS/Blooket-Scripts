"""
	This script gets info about the game, by joining with a fake player.
	It then uses that data to loop through each player in the game, and sends a request to kick them.
	This is the exact same as MassKick.py, although it allows you to choose a specific player to not kick.
"""

import requests, json

gamePin = str(input("Game pin: "))
nameToBypass = str(input("Who should not get kicked?: "))

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

# Send request to kick the fake player
r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name=blooketbad", headers={
	"Referer": "https://www.blooket.com/"
})

# Get a list of players
players = json.loads(joinText)["host"]["c"].keys()
# For each player in the game
for playerName in players:
	# Skip specific player
	if not nameToBypass in playerName:
		# Send request to kick the player
		r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={playerName}", headers={
			"Referer": "https://www.blooket.com/"
		})
