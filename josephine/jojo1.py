# main.py
from jojo import Food, Matooke, Plantain, Yellowbananas, Mabungo

matooke = Matooke("matoke", "green", "mpologoma", "medium")
matooke.details()
matooke.tasteless()

plantain = Plantain("plantain", "yellow", "gonja", "small")
plantain.details()
plantain.sweet()

yellowbananas = Yellowbananas("yellowbananas", "yellow", "bogoya", "big")
yellowbananas.details()
yellowbananas.sweet()

mabungo = Mabungo("mabungo", "bananas", "yellow", "bigger")
mabungo.details()
mabungo.sweet()
mabungo.sweeter()
