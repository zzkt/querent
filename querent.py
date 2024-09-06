#!/usr/bin/env python

# File name: querent.py
# Description: An experimental software tool for personal tarot practice.
# Author: nik gaffney <nik@fo.am>
# Created: 2024-09-06
# SPDX-License-Identifier: GPL-3.0-or-later

import random
import json

def parse_interpretations(path):
    with open(path) as f:
        data = json.load(f)
        return data

major_arcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Justice", "The Hermit", "The Wheel of Fortune", "Strength", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]

suits = ["Wands", "Swords", "Cups", "Pentacles"]

ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Page", "Knight", "Queen", "King"]

minor_arcana = [f"{card} of {suit}" for card in ranks for suit in suits]

deck = major_arcana + minor_arcana

interpretation = parse_interpretations("data/card_meanings.json")

def prepare_the_cards():
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def spread_cards(deck):
    spread = deck[0:3]
    return spread

def interpret_spread(spread):
    positions = ["ANCHOR: The present situation, what grounds you.",
                 "TIDE: The changing influences, what's in flux.",
                 "HORIZON: The long-term outlook, what's ahead."]
    for i in range(3):
        card = spread[i]
        print(f"{positions[i]}\n{card}: {interpretation[card]}\n")

def read_cards():
    deck = prepare_the_cards()
    shuffle_deck(deck)
    spread = spread_cards(deck)
    interpret_spread(spread)

if __name__ == '__main__':
    read_cards()
