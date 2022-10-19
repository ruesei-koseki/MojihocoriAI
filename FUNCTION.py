import MEMORY

import atexit
def allDone():
    print("セーブします")
    MEMORY.save()
    print("完了")
atexit.register(allDone)
