
import os, sys
import inspect
import importlib.util

from logics.board import *
from logics.hero import *
from logics.hand import *
from logics.card import *

from engine.engine_util import *

def init_game(players_count: int) -> list:
    re = map( Hero, range(players_count) )
    return list(re)

def load_card(path_to_card_module: str) -> Card:
    mod = load_dynamic_to_sys(path_to_card_module)
    card_class = get_last_class_from_module(mod)
    card = card_class()
    return card

def load_card_for_hero(hero : Hero, path_to_card_module: str) -> Card:
    card = load_card(path_to_card_module)
    hero.hand.add_card(card)
    return card


