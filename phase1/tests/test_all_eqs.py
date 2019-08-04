# -*- coding: UTF-8 -*-
import random
import sys

sys.path.append('..')
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_eq_move import EQMove

test_eq=EQDefense()
test_eq.show_me()
test_eq.show_me_unique()

test_eq=EQAttack()
test_eq.show_me()
test_eq.show_me_unique()

test_eq=EQMana()
test_eq.show_me()
test_eq.show_me_unique()

test_eq=EQMove()
test_eq.show_me()
test_eq.show_me_unique()
