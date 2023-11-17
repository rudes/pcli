import json

from pathlib import Path

pokemon = []
for file in Path("info").iterdir():
	if file.is_dir():
		continue
	with file.open() as f:
		pokemon.append(json.load(f))

moves = []
for file in Path("info/skills").iterdir():
	with file.open() as f:
		moves.append(json.load(f))

with open("pokemon.json", "w") as out:
	out.write(json.dumps(pokemon))

with open("moves.json", "w") as out:
	out.write(json.dumps(moves))