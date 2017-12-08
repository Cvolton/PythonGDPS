#this is basically absolutes seed2 generator but expanded for a few more stuff, so credits to him
import hashlib,base64

def Sha1(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode())
    return sha1.hexdigest()

def CharXor(text,keys):
    res = ''
    for i in range(len(text)):
        res += chr(ord(text[i])^ord(keys[i%len(keys)]))
    return res

def GetSeed2(lvlstr):
    mix = ''
    rep = len(lvlstr)//50
    for i in range(50):
        mix += (lvlstr[rep*i])
    return base64.b64encode(CharXor(Sha1(mix+'xI25fpAapCQg'),'41274').encode()).decode()

def GenSolo(lvlstr):
    mix = ''
    rep = len(lvlstr)//40
    for i in range(40):
        mix += (lvlstr[rep*i])
    return Sha1(mix+'xI25fpAapCQg')

def GenMulti(levellist):
    mix = ''
    for levelinfo in levellist:
        mix += str(levelinfo.levelid)[0] + str(levelinfo.levelid)[-1] + str(levelinfo.starstars) + str(levelinfo.starcoins)
    return Sha1(mix+'xI25fpAapCQg')
