"""
	This script gets the correct answers to each question in a Blooket game.
	Note that Blooket randomises the order of questions for each player.
"""

import requests, json, string, random, argparse

parser = argparse.ArgumentParser(description="Test")
parser.add_argument("-p", help="Game pin")

args = parser.parse_args()

gamePin = str(args.p)

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
if "msg" in json.loads(r.text) and json.loads(r.text)["msg"] == "no game":
	print("No game exists with that pin")
	exit()
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
answersList = "Answers:"
for question in questions:
	# Append the question and the first correct answer for the question to the output string
	answersList += f"\n{question['question']}: {question['correctAnswers'][0]}"
print(answersList)
