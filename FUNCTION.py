import MEMORY
import DATA

import atexit
def allDone():
    print("セーブします")
    MEMORY.saveData()
    print("完了")
atexit.register(allDone)