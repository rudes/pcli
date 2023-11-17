import sys
import argparse

from helpers import pokemon, pokelist, move, display

parser = argparse.ArgumentParser(
	prog='pcli',
	description='Query the PokeMMO Dex')

parser.add_argument('category', metavar='C', type=str,
	help="Category to search in")
parser.add_argument('terms', metavar='T', type=str, nargs="?",
	help="Term to search for in Category")
parser.add_argument('--json', action='store_true',
	help="Get output in JSON instead")

args = parser.parse_args()

if not args.terms:
	output = pokelist(args.category)
	display(args.category, output, args.json)
	sys.exit(0)

if args.category == 'move':
	output = move(args.terms)
	display(args.category, output, args.json)
	sys.exit(0)

output = pokemon(args.category, args.terms)
display(args.category, output, args.json)