#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    pokenum = input("Pick a number between 1 and 807: ")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi)

main()
