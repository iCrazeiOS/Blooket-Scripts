"""
	This script gets the correct answers to each question in a Blooket game.
	Note that Blooket randomises the order of questions for each player.
"""

import requests, json, string, random

gamePin = str(input("Game pin: "))
# Set name as a random string
name = ''.join(random.choices(string.ascii_letters+string.digits,k=9))

# Join the game with that name
r = requests.put("https://api.blooket.com/api/firebase/join", data={
	"id": gamePin,
	"name": name
}, headers={
	"Referer": "https://www.blooket.com/"
})

# Get gameID from the request response
firstPart = r.text.split('"set":"')[1]
gameID = firstPart[0:firstPart.index('"')]

# Kick our player
r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={name}", headers={
	"Referer": "https://www.blooket.com/"
})

# Use their API to find the list of questions/answers
r = requests.get(f"https://api.blooket.com/api/games?gameId={gameID}")
questions = json.loads(r.text)["questions"]
# For each question in the array
for question in questions:
	# Print the question, and thefirst correct answer for the question
	print(f"{question['question']}: {question['correctAnswers'][0]}")
