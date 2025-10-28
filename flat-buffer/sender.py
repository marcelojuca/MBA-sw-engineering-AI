# sender.py
import flatbuffers
from mygame.Monster import MonsterStart, MonsterAddPos, MonsterAddMana, MonsterAddHp
from mygame.Monster import MonsterAddName, MonsterAddInventory, MonsterAddColor, MonsterEnd
from mygame.Monster import MonsterStartInventoryVector
from mygame.Vec3 import CreateVec3
from mygame import Color

def create_monster():
    # 1. Start a new builder (size hint optional)
    builder = flatbuffers.Builder(1024)

    # 2. Create nested objects first
    name = builder.CreateString('Orc')

    # Inventory vector of bytes
    MonsterStartInventoryVector(builder, 5)
    for b in [4, 3, 2, 1, 0][::-1]:      # push in reverse order!
        builder.PrependByte(b)
    inventory = builder.EndVector()

    # Position struct
    pos = CreateVec3(builder, 1.0, 2.0, 3.0)

    # 3. Build the table
    MonsterStart(builder)
    MonsterAddPos(builder, pos)
    MonsterAddMana(builder, 150)
    MonsterAddHp(builder, 80)
    MonsterAddName(builder, name)
    MonsterAddInventory(builder, inventory)
    MonsterAddColor(builder, Color.Color().Blue)
    monster = MonsterEnd(builder)

    # 4. Finish
    builder.Finish(monster)
    return builder.Output()   # returns bytes
