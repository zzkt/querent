#!/usr/bin/env python

# File name: main.py
# Description: An experimental software tool for personal tarot practice.
# Author: nik gaffney <nik@fo.am>
# Created: 2024-09-06
# SPDX-License-Identifier: GPL-3.0-or-later

import flet as ft
from querent import *

CARD_WIDTH = 360
CARD_HEIGHT = 600

TEXT_WIDTH = 360
TEXT_HEIGHT = 2160

PADDING = 40

def main(page: ft.Page):
    deck = prepare_cards()
    shuffle_deck(deck)
    spread = spread_cards(deck)
    reading = interpret_spread(spread)

    c1_text = reading[0]
    c2_text = reading[1]
    c3_text = reading[2]

    c1_image = cards[spread[0]]['image']
    c2_image = cards[spread[1]]['image']
    c3_image = cards[spread[2]]['image']

    page.fonts = {"Baskerville": "https://github.com/google/fonts/raw/main/ofl/librebaskerville/LibreBaskerville-Regular.ttf"}

    card_1 = ft.Stack(
        [
            ft.Image(
                src=c1_image,
                width=CARD_WIDTH,
                height=CARD_HEIGHT,
                top=PADDING,
                fit=ft.ImageFit.CONTAIN,
                border_radius=ft.border_radius.all(30),
            ),
            ft.Text(
                c1_text,
                size=14,
                font_family="Baskerville",
                color=ft.colors.GREY_600,
                top=CARD_HEIGHT + 2*PADDING,
                width=TEXT_WIDTH,
                text_align="left",
                overflow="VISIBLE"
            )
        ],
        alignment=ft.alignment.top_center,
        left=PADDING,
        width=TEXT_WIDTH,
        height=CARD_HEIGHT + TEXT_HEIGHT,
    )

    card_2 = ft.Stack(
        [
            ft.Image(
                src=c2_image,
                width=CARD_WIDTH,
                height=CARD_HEIGHT,
                top=PADDING,
                fit=ft.ImageFit.CONTAIN,
                border_radius=ft.border_radius.all(10),
            ),
            ft.Text(
                c2_text,
                size=14,
                font_family="Baskerville",
                color=ft.colors.GREY_600,
                top=CARD_HEIGHT + 2*PADDING,
                width=TEXT_WIDTH,
                text_align="left",
                overflow="VISIBLE"
            )
        ],
        alignment=ft.alignment.top_center,
        left=TEXT_WIDTH + 2*PADDING,
        width=TEXT_WIDTH,
        height=CARD_HEIGHT + TEXT_HEIGHT,
    )

    card_3 = ft.Stack(
        [
            ft.Image(
                src=c3_image,
                width=CARD_WIDTH,
                height=CARD_HEIGHT,
                top=PADDING,
                fit=ft.ImageFit.CONTAIN,
                border_radius=ft.border_radius.all(10),
            ),
            ft.Text(
                c3_text,
                size=14,
                font_family="Baskerville",
                color=ft.colors.GREY_600,
                top=CARD_HEIGHT + 2*PADDING,
                width=TEXT_WIDTH,
                text_align="left",
                overflow="VISIBLE"
            )
        ],
        alignment=ft.alignment.top_center,
        left=2*TEXT_WIDTH + 3*PADDING,
        width=TEXT_WIDTH,
        height=CARD_HEIGHT + TEXT_HEIGHT,
    )

    controls = [card_1, card_2, card_3]

    page.title = "querent"

    page.window.full_screen = True

    page.scroll="HIDDEN"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(ft.Stack(controls=controls,
                      width=3*TEXT_WIDTH + 5*PADDING,
                      height=CARD_HEIGHT + TEXT_HEIGHT + 2*PADDING
                      ))

ft.app(main, assets_dir="data")
