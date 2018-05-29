import requests
# pip install cryptography
# pip install pyOpenSSL
# pip install certifi

import os
import config


class lychee:
    # session
    baseUrl = config.lycheeServer
    baseIndexUrl = baseUrl + "/php/index.php"
    userName = config.username
    password = config.password

    albumIDCache = {}
    photoUrlCache = {}

    def __init__(self, albumName="defaultAlbum"):
        self.albumName = albumName
        self.session = requests.Session()
        self.__login()

    def __login(self):
        payload = {'function': 'Session::login', "password": self.password, "user": self.userName}
        r = self.session.post(self.baseIndexUrl, data=payload)
        if(not r.json()):
            raise Exception("password error")




    def getUrlStr(self, localUrl):
        if(self.photoUrlCache.__contains__(localUrl)):
            return self.photoUrlCache[localUrl]

        url = self.__upload(localUrl, self.albumName)
        self.albumIDCache[localUrl] = url

        return url

    def __upload(self, localUrl, albumName):
        albumId = self.getAlbumId(albumName)
        payload = {'function': 'Photo::add', "albumID": albumId}
        # os.path.basename(localUrl)
        # 中文文件名在requests发包时会出错
        fileJson = {"0": ("fileName" + os.path.splitext(localUrl)[1], open(localUrl, 'rb'))}

        r = self.session.post(self.baseIndexUrl, data=payload, files=fileJson)
        if(r.json()):
            photoId = r.json()
            payload = {'function': 'Photo::get', 'albumID': albumId, "photoID": photoId}
            r = self.session.post(self.baseIndexUrl, data=payload)
            return self.baseUrl + "/" + r.json()["url"]
        else:
            print("upload fail")
            return localUrl

    def getAlbumId(self, albumName, isAutoCreate=True):
        if(self.albumIDCache.__contains__(albumName)):
            return self.albumIDCache[albumName]

        try:
            payload = {'function': 'Albums::get'}
            r = self.session.post(self.baseIndexUrl, data=payload)
            jsonResp = r.json()
            if (jsonResp['albums']):
                for album in jsonResp['albums']:
                    self.albumIDCache[album["title"]] = album["id"]
        except AttributeError:
            print("jsonError")
        except KeyError:
            print("jsonError")
        except TypeError:
            print("jsonError")
        finally:
            pass

        if(self.albumIDCache.__contains__(albumName)):
            return self.albumIDCache[albumName]

        if(not isAutoCreate):
            return 0

        payload = {'function': 'Album::add', 'title': albumName}
        r = self.session.post(self.baseIndexUrl, data=payload)
        if(isinstance(r.json(), int)):
            self.albumIDCache[albumName] = r.json()
            return r.json()

        raise Exception("create album error")

