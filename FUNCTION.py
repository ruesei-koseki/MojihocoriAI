import MEMORY
import DATA

import atexit
def allDone():
    print("セーブします")
    DATA.data["tangoOkikae1"] = DATA.tangoOkikae1
    DATA.data["tangoOkikae2"] = DATA.tangoOkikae2
    MEMORY.saveData()
    print("完了")
atexit.register(allDone)