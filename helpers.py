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
	if "." in category:
		category, key = category.split(".")
	if not key:
		return [i for i in poke_json if terms in i[category]]
	output = []
	for p in poke_json:
		if isinstance(p[category], list):
			for c in p[category]:
				if terms in c[key]:
					output.append(p)
		if isinstance(p[category], dict):
			print(p[category])
			if terms in p[category][key]:
				output.append(p)
	return output

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
		table = Table(title=f"{category.title()} Search")
		table.add_column("ID", justify="right")
		table.add_column("Name")
		table.add_column("Types")
		table.add_column("Base Stats")
		output = list({p['id']:p for p in output}.values())
		output.sort(reverse = True, key=lambda x : x["stats"]["speed"])
		for d in output:
			unique_types = list(set(d["types"]))
			table.add_row(
				str(d["id"]),
				d["name"],
				",".join(unique_types).title(),
				_flatten_stats(d["stats"]),
			)
	console = Console()
	console.print(table)

def _flatten_stats(stats):
	r = f"{stats['hp']:3} |"
	r += f"{stats['attack']:4} |"
	r += f"{stats['defense']:4} |"
	r += f"{stats['sp_attack']:4} |"
	r += f"{stats['sp_defense']:4} |"
	r += f"{stats['speed']:4}"
	return r