"""
	This script sends a request to kick a specific player from the game.
"""

import requests, argparse

parser = argparse.ArgumentParser(description="Test")
parser.add_argument("-p", help="Game pin")
parser.add_argument("-n", help="Name to kick")

args = parser.parse_args()

gamePin = str(args.p)
name = str(args.n)

if gamePin == "None": gamePin = str(input("Game pin: "))
if name == "None": name = str(input("Name to kick: "))

# Sends request to kick the specified player
r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={name}", headers={
	"Referer": "https://www.blooket.com/"
})

print(r.text)
