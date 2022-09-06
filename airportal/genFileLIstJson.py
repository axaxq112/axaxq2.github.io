# 本程序用于生成 data/filelist.json
# 想要存储的文件全部放在files目录下（文件大小 <10MB 必须放于根目录）
# 生成json后，Commit 然后 Push Origin 即可
import os
from os import path
import random

def randomCode():
    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
    characters = random.sample(alphabet, 8)
    retStr = ''.join(characters)
    return retStr

def getFileListJson (url):
        retJson = {'files':[]}
        file  = os.listdir(url)
        for f in file:
                real_url = path.join (url , f)
                if path.isfile(real_url):
                        #存于指定根目录下的文件
                        absPath = path.abspath(real_url)
                        fileName = os.path.basename(absPath)
                        fileSuffix = os.path.splitext(fileName)[-1]  
                        print("检测到文件名: {} 扩展名: {} 完整路径:{}".format(fileName,fileSuffix,absPath))
                        retJson['files'].append({'file_url':fileName, 'code': randomCode()})
                else:
                        print("跳过文件夹: '{}'".format(f))
                        pass
        return str(retJson)

if __name__ == "__main__":
    a = getFileListJson("./files")
    print(a)