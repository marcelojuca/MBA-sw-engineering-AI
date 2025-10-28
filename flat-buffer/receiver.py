# receiver.py
from mygame.Monster import Monster
from mygame import Color

def read_monster(buf: bytes):
    monster = Monster.GetRootAs(buf, 0)   # zero-copy!

    # Direct access
    name = monster.Name()                # str
    hp   = monster.Hp()                  # int
    mana = monster.Mana()
    color = monster.Color()              # enum byte

    # Position struct
    pos = monster.Pos()
    x, y, z = pos.X(), pos.Y(), pos.Z()

    # Inventory vector
    inventory = [monster.Inventory(i) for i in range(monster.InventoryLength())]

    print(f"{name} hp:{hp} mana:{mana} pos:({x},{y},{z}) color:{color} inv:{inventory}")