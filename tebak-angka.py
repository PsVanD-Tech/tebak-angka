#100% Vanilla128#

import time
import random
from random import choice
import os
from os import system

os.system('clear')

a = "01234567890"
b = "01234567890"

all = a + b
#all Disini Untuk Dijadikan Angka Random
print("Tebak Nomor")
print("No Brp Yg Kau Tebak? 0-99 = ")
input()
angkar = ''.join(choice(all))
#angkar adalah angka random:v
print("Jawabannya adalah")
print(angkar)
