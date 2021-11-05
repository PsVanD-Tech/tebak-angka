#100% Vanilla128#

import time
import random
from random import choice
import os
from os import system

a="1234567890"
#A Disini Untuk Dijadikan Angka Random
print("Tebak Nomor")
print("No Brp Yg Kau Tebak? 0-9 = ")
input()
time.sleep(2)
angkar = ''.join(choice(a))
#angkar adalah angka random:v
print("Jawabannya adalah")
print(angkar)
