import sqlite3
bag = sqlite3.connect("a.vt")

cursor = bag.cursor()

bag.close()

