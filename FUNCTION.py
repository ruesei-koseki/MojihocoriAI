import MEMORY
import DATA

import atexit
def allDone():
    DATA.data["heart"] = DATA.heart
    print("セーブします")
    MEMORY.saveData()
    print("完了")
atexit.register(allDone)