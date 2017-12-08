from django.http import HttpResponse
from django.template import Context, Template
from django.template.loader import get_template
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from pythongdps.models import Levels, Dailyfeatures, Users
from random import randint
from datetime import datetime
from base64 import b64decode, b64encode
from time import time
from pythongdps.gamehandlers.mainlib import CharXor, GenSolo, Sha1, GenMulti

def getUserInfo(userID):
    userinfo = Users.objects.get(userid = userID)
    return str(userinfo.userid) + ":" + str(userinfo.username) + ":" + str(userinfo.extid)

@csrf_exempt
def download(request):
    try:
        #levelid = "-1"
        levelid = str(int(request.POST.get('levelID', '-1')))
        if levelid == "-1":
            dailyinfo = Dailyfeatures.objects.filter(timestamp__lte = time())
            dailyinfo = dailyinfo.order_by('-timestamp')[0]
            levelid = str(int(dailyinfo.levelid))
            feaid = dailyinfo.feaid
        else:
            feaid = 0
        levelstring = open('/var/www/html/a/data/levels/'+levelid,'r')
        levelinfo = Levels.objects.get(levelid = int(levelid))
        gameversion = int(request.POST.get('gameVersion', '0'))
    except:
        return HttpResponse("-1")
    if gameversion > 19:
        #2.0 onwards
        password = b64encode(CharXor(str(levelinfo.password),"26364").encode())
        password = password.decode("utf-8")
        levelDesc = levelinfo.leveldesc
    else:
        levelDesc = b64decode(levelinfo.leveldesc).decode("utf-8").split(":")[0]
        password = levelinfo.password
    levelstring = levelstring.read()
    gensolo = GenSolo(levelstring)
    somestring = get_template("levels/downloadSomeStr").render({'levelinfo': levelinfo,
                                                                'feaid': feaid})
    somehash = Sha1(somestring+"xI25fpAapCQg")
    if feaid != 0:
        somestring = getUserInfo(levelinfo.userid)
    return render(request, "levels/download", {'levelinfo': levelinfo,
                                               'levelDesc':levelDesc,
                                               'password':password,
                                               'genSolo':gensolo,
                                               'feaid':feaid,
                                               'someHash':somehash,
                                               'someString':somestring,
                                               'updatedate' : datetime.fromtimestamp(int(levelinfo.updatedate)),
                                               'uploaddate' : datetime.fromtimestamp(int(levelinfo.uploaddate)),
                                               'levelstring':levelstring})

@csrf_exempt
def search(request):
    try:
        searchtype = int(request.POST.get('levelID', '4'))
        offset = int(request.POST.get('page', '1')) * 10
        limit = offset + 10
    except:
        return HttpResponse("-1")
    levellist = Levels.objects.order_by('-uploaddate')[offset:limit]
    levelcount = Levels.objects.count()
    userstring = ""
    first = True
    for levelinfo in levellist:
        if not first:
            userstring += "|"
        else:
            first = False
        userstring += getUserInfo(levelinfo.userid)
    songstring = ""
    pageinfo = get_template("page").render({'count': levelcount,
                                            'offset': offset,
                                            'shown': 10})
    multihash = GenMulti(levellist)
    #users#songs#pageinfo#hash
    return render(request, "levels/get", {'levellist': levellist,
                                          'userstring': userstring,
                                          'songstring': songstring,
                                          'pageinfo': pageinfo,
                                          'hash': multihash})
