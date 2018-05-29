import re
import lychee
import requests
import sys
import os

reg = re.compile(r'!\[([^\]]*)\]\(([^\)]*)\)')
httpCheck = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@  # /%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')


def dealwithFile(sourceFile):
    dirname = os.path.dirname(sourceFile)
    tartgetFile = os.path.splitext(sourceFile)[0] + "_out" + os.path.splitext(sourceFile)[1]
    albumName = os.path.basename(dirname)
    print("album name is ", albumName)
    uploader = lychee.lychee(albumName=albumName)

    def imageRepl(match):
        matchStr = match.group()

        picUrl = match.group(2)
        if(httpCheck.match(picUrl)):
            print("already Url skip:", match.group(2))
            return matchStr

        if(not os.path.isfile(picUrl)):
            picUrl = dirname + picUrl

        if(not os.path.isfile(picUrl)):
            print("not exchange file not exist:", match.group(2))
            return matchStr

        try:
            targetUrl = uploader.getUrlStr(picUrl)
        except Exception:
            print("not exchange upload fail:", match.group(2))
            return matchStr

        if(httpCheck.match(targetUrl)):
            print("exchange:", match.group(2), " -> ", targetUrl)
            return matchStr.replace(match.group(2), targetUrl)
        else:
            print("not exchange upload url error:", match.group(2),  " X-X ", targetUrl)
            return matchStr

    with open(sourceFile, "r", encoding="utf8") as f, open(tartgetFile, "w", encoding="utf8") as f2:
        for line in f:
            newLine = reg.sub(imageRepl, line)
            f2.write(newLine)


sourceFile = sys.argv[1]
dealwithFile(sourceFile)
