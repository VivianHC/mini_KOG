# -*- coding: UTF-8 -*-

import random
import sys
sys.path.append('..')
from package_KingOfGlory.class_hero import Hero
print('\n---测试产生一批英雄---')
for i in range(10):
    hero=Hero()
    hero.show_me()
