import sys
import json

from rich.console import Console
from rich.table import Table

with open("data/pokemon.json") as f:
	poke_json = json.load(f)
with open("data/moves.json") as f:
	moves_json = json.load(f)

if not poke_json or not moves_json:
	sys.exit(1)

def pokelist(category):
	return list({i[category] for i in poke_json})

def pokemon(category, terms):
	return [i for i in poke_json if terms in i[category]]

def move(terms):
	return [i for i in moves_json if terms in i["name"]]

def display(category, output, json_flag):
	if json_flag:
		print(json.dumps(output))
		return
	if category == "move":
		table = Table(title="Move Info")
		table.add_column("Key", justify="right")
		table.add_column("Value")
		move_data = output[0]
		for d in move_data:
			table.add_row(d, str(move_data[d]))
	else:
		table = Table(title=f"{category.title()} search")
		table.add_column("ID", justify="right")
		table.add_column("Name")
		table.add_column("Types")
		table.add_column(category.title())
		output.sort(key=lambda x : x["id"])
		for d in output:
			types = ",".join(d["types"]).title()
			table.add_row(str(d["id"]), d["name"], types, str(d[category]))
	console = Console()
	console.print(table)