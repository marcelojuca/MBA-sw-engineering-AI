# demo.py
from sender import create_monster
from receiver import read_monster

buf = create_monster()
print("Buffer size:", len(buf), "bytes")
read_monster(buf)