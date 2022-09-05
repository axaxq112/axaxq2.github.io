# 本程序用于生成 data/filelist.json
# 想要存储的文件全部放在files目录下（文件大小 <10MB 必须放于根目录）
# 生成json后，Commit 然后 Push Origin 即可

import os
import json
import time

def sleepTime(hour, min, sec):
    t = hour * 3600 + min * 60 + sec
    time.sleep(t)

def log(contentStr,timeFormat = "%Y-%m-%d %H:%M:%S"):
    now = int(time.time())
    timeStruct = time.localtime(now)
    strTime = time.strftime(timeFormat, timeStruct)
    print("[" + strTime + "]"  + contentStr)
    return strTime

if __name__ == "__main__":
    log("Start")