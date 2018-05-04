
import os, sys
import inspect
import importlib.util

from logics.board import *
from logics.hero import *
from logics.hand import *

from engine.engine_util import *

def init_game(players_count: int) -> list:
    re = map( Hero, range(players_count) )
    return list(re)

def load_card_for_hero(hero, path_to_card_module: str):
    mod = load_dynamic(path_to_card_module)
    card_class = get_last_class_from_module(mod)
    card = card_class()
    hero.hand.add_card(card)
    
    return card