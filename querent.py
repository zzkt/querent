#!/usr/bin/env python

# File name: querent.py
# Description: An experimental software tool for personal tarot practice.
# Author: nik gaffney <nik@fo.am>
# Created: 2024-09-06
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import json

cards_file = "data/cards_thoth.json"

def parse_cards_file(path):
    with open(path) as f:
        data = json.load(f)
        return data

cards = parse_cards_file(cards_file)

def prepare_cards():
    global cards
    deck = list(set(cards))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def spread_cards(deck):
    spread = deck[0:3]
    return spread

def interpret_spread(spread):
    global cards
    layout = ["TIDE: The changing influences, what's in flux.",
              "ANCHOR: The present situation, what grounds you.",
              "HORIZON: The long-term outlook, what's ahead."]
    result = []
    for i in range(3):
        card = spread[i]
        result.append(f"{layout[i]}\n\n{card}: {cards[card]['interpretation']}\n")
    return result

def read_cards():
    deck = prepare_cards()
    shuffle_deck(deck)
    spread = spread_cards(deck)
    reading = interpret_spread(spread)
    print(*reading, sep="\n")

if __name__ == '__main__':
    read_cards()
