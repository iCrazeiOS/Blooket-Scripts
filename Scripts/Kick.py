"""
	This script sends a request to kick a specific player from the game.
"""

import requests

gamePin = str(input("Game pin: "))
name = str(input("Name to kick: "))

# Sends request to kick the specified player
r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={name}", headers={
	"Referer": "https://www.blooket.com/"
})

print(r.text)
