import MEMORY

import atexit
def allDone():
    print("セーブします")
    MEMORY.saveData()
    print("完了")
atexit.register(allDone)