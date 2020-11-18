#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    #pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/ditto").json()
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/1").json()

    print(pokeapi['sprites']['front_default'])

main()
