# -*- coding: utf-8 -*-

from gyevha import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
 
# Ini Untuk Login Via Lik Dan Via Emal
#gye = LINE()
#gye = LINE("Email","Password")
#gye.log("Auth Token : " + str(gye.authToken))
#channelToken = gye.getChannelResult()
#gye.log("Channel Token : " + str(channelToken))

# Silahkan Edit Sesukamu
# Asalkan Rapih Dan Respon
# jika ingin login Via qr Ganti Saja
# Atau Login Via Emal
# Mudeng Orang kalo Ra Mudeng
# Sungguh Terlalu
# Jangan Lupa Add Admin 
# id Line ( aisyagye )
#==============================================================================#
botStart = time.time()
#kalo mau login code qr disini pake
gye = LINE()
gye.log("Auth Token : " + str(gye.authToken))
channelToken = gye.getChannelResult()
gye.log("Channel Token : " + str(channelToken))

ais = LINE()
ais.log("Auth Token : " + str(ais.authToken))
channelToken = ais.getChannelResult()
ais.log("Channel Token : " + str(channelToken))

ki2 = LINE()
ki2.log("Auth Token : " + str(ki2.authToken))
channelToken = ki2.getChannelResult()
ki2.log("Channel Token : " + str(channelToken))

ki3 = LINE()
ki3.log("Auth Token : " + str(ki3.authToken))
channelToken = ki3.getChannelResult()
ki3.log("Channel Token : " + str(channelToken))

ki4 = LINE()
ki4.log("Auth Token : " + str(gye.authToken))
channelToken = ki4.getChannelResult()
ki4.log("Channel Token : " + str(channelToken))

ki5 = LINE()
ki5.log("Auth Token : " + str(gye.authToken))
channelToken = ki5.getChannelResult()
ki5.log("Channel Token : " + str(channelToken))

ki6 = LINE()
ki6.log("Auth Token : " + str(gye.authToken))
channelToken = ki6.getChannelResult()
ki6.log("Channel Token : " + str(channelToken))

ki7 = LINE()
ki7.log("Auth Token : " + str(gye.authToken))
channelToken = ki7.getChannelResult()
ki7.log("Channel Token : " + str(channelToken))

ki8 = LINE()
ki8.log("Auth Token : " + str(gye.authToken))
channelToken = ki8.getChannelResult()
ki8.log("Channel Token : " + str(channelToken))

ki9 = LINE()
ki9.log("Auth Token : " + str(gye.authToken))
channelToken = ki9.getChannelResult()
ki9.log("Channel Token : " + str(channelToken))

ki10 = LINE()
ki10.log("Auth Token : " + str(gye.authToken))
channelToken = ki10.getChannelResult()
ki10.log("Channel Token : " + str(channelToken))

ki11 = LINE()
ki11.log("Auth Token : " + str(gye.authToken))
channelToken = ki11.getChannelResult()
ki11.log("Channel Token : " + str(channelToken))

ki12 = LINE()
ki12.log("Auth Token : " + str(gye.authToken))
channelToken = ki12.getChannelResult()
ki12.log("Channel Token : " + str(channelToken))

ki13 = LINE()
ki13.log("Auth Token : " + str(gye.authToken))
channelToken = ki13.getChannelResult()
ki13.log("Channel Token : " + str(channelToken))

ki14 = LINE()
ki14.log("Auth Token : " + str(gye.authToken))
channelToken = ki14.getChannelResult()
ki14.log("Channel Token : " + str(channelToken))

ki15 = LINE()
ki15.log("Auth Token : " + str(gye.authToken))
channelToken = ki15.getChannelResult()
ki15.log("Channel Token : " + str(channelToken))

ki16 = LINE()
ki16.log("Auth Token : " + str(gye.authToken))
channelToken = ki16.getChannelResult()
ki16.log("Channel Token : " + str(channelToken))

ki17 = LINE()
ki17.log("Auth Token : " + str(gye.authToken))
channelToken = ki17.getChannelResult()
ki17.log("Channel Token : " + str(channelToken))

ki18 = LINE()
ki18.log("Auth Token : " + str(gye.authToken))
channelToken = ki18.getChannelResult()
ki18.log("Channel Token : " + str(channelToken))

ki19 = LINE()
ki19.log("Auth Token : " + str(gye.authToken))
channelToken = ki19.getChannelResult()
ki19.log("Channel Token : " + str(channelToken))

ki20 = LINE()
ki20.log("Auth Token : " + str(gye.authToken))
channelToken = ki20.getChannelResult()
ki20.log("Channel Token : " + str(channelToken))

#kalo mau login menggunakan token
#gunakan disini hapus tanda pagarnya 
#yg atas dinpagar atau bisa juga token di atas 
#di dalam tanda LINE ("TOKEN MU ")
#gye = LINE("Et6qM8UeTce5bGsZG4te.ee6vQU/1ppqr93nt9QLUZG.b5fsCbuxW7zZRtrK5U/74k/53Abd5dWPxfdtLy9bL9I=")
#ais = LINE("Etska0dbjsHvPgZKwmj9.EikS5M3O+L4fOqxjjVgLsq.KlWfvmGVaXdM0yvKM8WGKARpcbAbiKVF9yORPt8QBJw=")
#ki2 = LINE("EtQsqzdJMWn73m72Gup0.OdjJmVnqXLeaZxpJzxDMOa.Z+6ApCht+0H1NeyX50QMD0Yq8oIhYyJ14Yg2yoM/tfc=")
#ki3 = LINE("EtDOOeYj4Rvl5PVfOEaa.ETpCu8czFapUIJQDqIA82G.tcOaI+VmHhWwMbyDL/7yXupWfdIvUJh80yWzu/UJXp8=")
#ki4 = LINE("EtWyu42OHWKSaxPHY3yd.jTri3xzV4E2Z1xvWxjTrRq.s1oy5gbYMT2haZV7l6yzV0bp5gONcnu+bGSSJ1mbT0c=")

KAC = [gye,ais,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20]
GUE = [ais,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20] # ini jangan luh hapus peak ini fungsi Ciak alias kick
#maksudnya agar bot sb/induk gak ikutan nge kick Mudeng ora
gyeMID = gye.profile.mid
aisMID = ais.profile.mid
ki2MID = ki2.profile.mid
ki3MID = ki3.profile.mid
ki4MID = ki4.profile.mid
ki5MID = ki5.profile.mid
ki6MID = ki6.profile.mid
ki7MID = ki7.profile.mid
ki8MID = ki8.profile.mid
ki9MID = ki9.profile.mid
ki10MID = ki10.profile.mid
ki11MID = ki11.profile.mid
ki12MID = ki12.profile.mid
ki13MID = ki13.profile.mid
ki14MID = ki14.profile.mid
ki15MID = ki15.profile.mid
ki16MID = ki16.profile.mid
ki17MID = ki17.profile.mid
ki18MID = ki18.profile.mid
ki19MID = ki19.profile.mid
ki20MID = ki20.profile.mid
Bots = [gyeMID,aisMID,ki2MID,ki3MID,ki4MID,ki5MID,ki6MID,ki7MID,ki8MID,ki9MID,ki10MID,ki11MID,ki12MID,ki13MID,ki14MID,ki15MID,ki16MID,ki17MID,ki18MID,ki19MID,ki20MID] #ini jangan dinrubah Gunanya agar bot tidak saling kick
creator = ["u104e95aaefb53cf411f77353f6a96ece"]
Owner = ["u104e95aaefb53cf411f77353f6a96ece"]
admin = ["u104e95aaefb53cf411f77353f6a96ece"]

gyeProfile = gye.getProfile()
aisProfile = ais.getProfile()
ki2Profile = ki2.getProfile()
ki3Profile = ki3.getProfile()
ki4Profile = ki4.getProfile()
ki5Profile = ki5.getProfile()
ki6Profile = ki6.getProfile()
ki7Profile = ki7.getProfile()
ki8Profile = ki8.getProfile()
ki9Profile = ki9.getProfile()
ki10Profile = ki10.getProfile()
ki11Profile = ki11.getProfile()
ki12Profile = ki12.getProfile()
ki13Profile = ki13.getProfile()
ki14Profile = ki14.getProfile()
ki15Profile = ki15.getProfile()
ki16Profile = ki16.getProfile()
ki17Profile = ki17.getProfile()
ki18Profile = ki18.getProfile()
ki19Profile = ki19.getProfile()
ki20Profile = ki20.getProfile()

lineSettings = gye.getSettings()
aisSettings = ais.getSettings()
ki2Settings = ki2.getSettings()
ki3Settings = ki3.getSettings()
ki4Settings = ki4.getSettings()
ki5Settings = ki5.getSettings()
ki6Settings = ki6.getSettings()
ki7Settings = ki7.getSettings()
ki8Settings = ki8.getSettings()
ki9Settings = ki9.getSettings()
ki10Settings = ki10.getSettings()
ki11Settings = ki11.getSettings()
ki12Settings = ki12.getSettings()
ki13Settings = ki13.getSettings()
ki14Settings = ki14.getSettings()
ki15Settings = ki15.getSettings()
ki16Settings = ki16.getSettings()
ki17Settings = ki17.getSettings()
ki18Settings = ki18.getSettings()
ki19Settings = ki19.getSettings()
ki20Settings = ki20.getSettings()

oepoll = OEPoll(gye)
oepoll1 = OEPoll(ais)
oepoll2 = OEPoll(ki2)
oepoll3 = OEPoll(ki3)
oepoll4 = OEPoll(ki4)
oepoll5 = OEPoll(ki5)
oepoll6 = OEPoll(ki6)
oepoll7 = OEPoll(ki7)
oepoll8 = OEPoll(ki8)
oepoll9 = OEPoll(ki9)
oepoll10 = OEPoll(ki10)
oepoll11 = OEPoll(ki11)
oepoll12 = OEPoll(ki12)
oepoll13 = OEPoll(ki13)
oepoll14 = OEPoll(ki14)
oepoll15 = OEPoll(ki15)
oepoll16 = OEPoll(ki16)
oepoll17 = OEPoll(ki17)
oepoll18 = OEPoll(ki18)
oepoll19 = OEPoll(ki19)
oepoll20 = OEPoll(ki20)

responsename = gye.getProfile().displayName
responsename1 = ais.getProfile().displayName
responsename2 = ki2.getProfile().displayName
responsename3 = ki3.getProfile().displayName
responsename4 = ki4.getProfile().displayName
responsename5 = ki5.getProfile().displayName
responsename6 = ki6.getProfile().displayName
responsename7 = ki7.getProfile().displayName
responsename8 = ki8.getProfile().displayName
responsename9 = ki9.getProfile().displayName
responsename10 = ki10.getProfile().displayName
responsename11 = ki11.getProfile().displayName
responsename12 = ki12.getProfile().displayName
responsename13 = ki13.getProfile().displayName
responsename14 = ki14.getProfile().displayName
responsename15 = ki15.getProfile().displayName
responsename16 = ki16.getProfile().displayName
responsename17 = ki17.getProfile().displayName
responsename18 = ki18.getProfile().displayName
responsename19 = ki19.getProfile().displayName
responsename20 = ki20.getProfile().displayName
#==============================================================================#




with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = gyeProfile.displayName
myProfile["statusMessage"] = gyeProfile.statusMessage
myProfile["pictureStatus"] = gyeProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    gye.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        gye.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "        Help1" + "\n" + \
                  "╭════════╬♥" + "\n" + \
                  "║͜͡☆➣ Help1 " + "\n" + \
                  "║͜͡☆➣ Help2 " + "\n" + \
                  "║͜͡☆➣ Help3 " + "\n" + \
                  "╰════════╬♥" + "\n" + \
                  "╭════════╬♥" + "\n" + \
                  "║͜͡☆➣ แทค (แทคทั้งห้อง)" + "\n" + \
                  "║͜͡☆➣ เข้ามา. ( สั่งบอทเข้าห้อง ) " + "\n" + \
                  "║͜͡☆➣ ออก. (สั่งบอทออก) " + "\n" + \
                  "║͜͡☆➣ บาย.(ออกหมดทั้งคนทั้งบอท) " + "\n" + \
                  "║͜͡☆➣ เตะ @ (สั่งบอทเตะออก)" + "\n" + \
                  "║͜͡☆➣ เตะดึก @ (สั่งบอทเตะ)" + "\n" + \
                  "║͜͡☆➣ คท " + "\n" + \
                  "║͜͡☆➣ Sp " + "\n" + \
                  "║͜͡☆➣ เชคค่า " + "\n" + \
                  "║͜͡☆➣ บอท " + "\n" + \
                  "║͜͡☆➣ รีบอท " + "\n" + \
                  "║͜͡☆➣ พูด (ใส่ข้อคาม)" + "\n" + \
                  "║͜͡☆➣ เขียน (ใส่ข้อคาม)" + "\n" + \
                  "║͜͡☆➣ เรา " + "\n" + \
                  "║͜͡☆➣ รายชื่อคนในห้อง " + "\n" + \
                  "║͜͡☆➣ เชคบอท " + "\n" + \
                  "╰════════╬♥" + "\n" + \
                  "╭════════╬♥" + "\n" + \
                  "║͜͡☆➣ Maibotline " + "\n" + \
                  "╰════════╬♥"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "  Help2 " + "\n" + \
                  "╭════════╬♥" + "\n" + \
                  "║͜͡☆➣ Pro on/off" + "\n" + \
                  "║͜͡☆➣ Pt on/off" + "\n" + \
                  "║͜͡☆➣ Qr on/off" + "\n" + \
                  "║͜͡☆➣ Iv on/off" + "\n" + \
                  "║͜͡☆➣ Cc on/off" + "\n" + \
                  "║͜͡☆➣ Add on/off" + "\n" + \
                  "║͜͡☆➣ Join on/off" + "\n" + \
                  "║͜͡☆➣ Leave on/off" + "\n" + \
                  "║͜͡☆➣ Sticker on/off" + "\n" + \
                  "║͜͡☆➣ Read on/off" + "\n" + \
                  "║͜͡☆➣ Dm on/off" + "\n" + \
                  "║͜͡☆➣ link on/off" + "\n" + \
                  "╰════════╬♥" + "\n" + \
                  "╭════════╬♥" + "\n" + \
                  "║͜͡☆➣ คนสร้างห้อง" + "\n" + \
                  "║͜͡☆➣ ไอดีห้อง" + "\n" + \
                  "║͜͡☆➣ ชื่อห้อง" + "\n" + \
                  "║͜͡☆➣ รายชื่อห้อง" + "\n" + \
                  "║͜͡☆➣ เชคห้อง" + "\n" + \
                  "║͜͡☆➣ ลิ้งห้อง" + "\n" + \
                  "║͜͡☆➣ #เปิดลิ้ง" + "\n" + \
                  "║͜͡☆➣ #ปิดลิ้ง" + "\n" + \
                  "║͜͡☆➣ พิมตาม on/off " + "\n" + \
                  "║͜͡☆➣ รายชื่อพิมตาม " + "\n" + \
                  "║͜͡☆➣ เพิ่มพิมตาม" + "\n" + \
                  "║͜͡☆➣ ลบพิมตาม" + "\n" + \
                  "║͜͡☆➣ เปิดอ่าน " + "\n" + \
                  "║͜͡☆➣ ปิดอ่าน " + "\n" + \
                  "║͜͡☆➣ ลบเวลาอ่าน " + "\n" + \
                  "║͜͡☆➣ คนอ่าน" + "\n" + \
                  "╰════════╬♥" + "\n" + \
                  "╭════════╬♥" + "\n" + \
                  "║͜͡☆➣ Maibotline " + "\n" + \
                  "╰════════╬♥"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "   Help3 " + "\n" + \
                  "╭════════╬♥" + "\n" + \
                  "║͜͡☆➣ แบน(ลงคอนแทคที่จะแบน)" + "\n" + \
                  "║͜͡☆➣ เชคแบน" + "\n" + \
                  "║͜͡☆➣ ล้างแบน" + "\n" + \
                  "║͜͡☆➣ รีบอท" + "\n" + \
                  "║͜͡☆➣ บอท " + "\n" + \
                  "║͜͡☆➣ มี " + "\n" + \
                  "║͜͡☆➣ มิด" + "\n" + \
                  "║͜͡☆➣ มิด @" + "\n" + \
                  "║͜͡☆➣ ชื่อ" + "\n" + \
                  "║͜͡☆➣ ตัส" + "\n" + \
                  "║͜͡☆➣ รูป" + "\n" + \
                  "║͜͡☆➣ รูปวีดีโอ" + "\n" + \
                  "║͜͡☆➣ รูปปก" + "\n" + \
                  "║͜͡☆➣ คท @" + "\n" + \
                  "║͜͡☆➣ มิด @" + "\n" + \
                  "║͜͡☆➣ ชื่อ @「Mention」" + "\n" + \
                  "║͜͡☆➣ ตัส @" + "\n" + \
                  "║͜͡☆➣ รูป @" + "\n" + \
                  "║͜͡☆➣ รูปวีดีโอ @" + "\n" + \
                  "║͜͡☆➣ รูปปก @" + "\n" + \
                  "║͜͡☆➣ คนสร้างห้อง" + "\n" + \
                  "║͜͡☆➣ ไอดีห้อง" + "\n" + \
                  "║͜͡☆➣ ชื่อห้อง" + "\n" + \
                  "║͜͡☆➣ รูปห้อง" + "\n" + \
                  "║͜͡☆➣ ลิ้งห้อง" + "\n" + \
                  "║͜͡☆➣ #เปิดลิ้ง" + "\n" + \
                  "║͜͡☆➣ รายชื่อห้อง" + "\n" + \
                  "║͜͡☆➣ #ปิดลิ้ง" + "\n" + \
                  "║͜͡☆➣ เชคห้อง" + "\n" + \
                  "║͜͡☆➣ เตะ @" + "\n" + \
                  "╰════════╬♥" + "\n" + \
                  "╭════════╬♥" + "\n" + \
                  "║͜͡☆➣ Maibotline " + "\n" + \
                  "╰════════╬♥"
    return helpTranslate
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] GYEVHA BOTS SATU")
            return
#-------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        gye.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        gye.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 25:
            print ("[ 25 ] GYEVHA BOTS TIGA")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != gye.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'h1':
                    helpMessage = helpmessage()
                    gye.sendMessage(to, str(helpMessage))
                    gye.sendContact(to,)
                    gye.sendMessage(to,)
                elif text.lower() == 'h2':
                    helpTextToSpeech = helptexttospeech()
                    gye.sendMessage(to, str(helpTextToSpeech))
                    gye.sendMessage(to,)
                elif text.lower() == 'h3':
                    helpTranslate = helptranslate()
                    gye.sendMessage(to, str(helpTranslate))
                    gye.sendMessage(to,)
#==============================================================================#
                elif text.lower() == 'sp':
                    start = time.time()
                    gye.sendMessage(to, "ความเร็วอยู่ที่...")
                    elapsed_time = time.time() - start
                    gye.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'รีบอท':    
                    gye.sendMessage(to, "Please Wait...")
                    time.sleep(5)
                    gye.sendMessage(to, "Restart Sukses")
                    restartBot()
                elif text.lower() == 'ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    gye.sendMessage(to, "login bot selama {}".format(str(runtime)))
                elif text.lower() == 'เรา':
                    try:
                        arr = []
                        owner = "u104e95aaefb53cf411f77353f6a96ece"
                        creator = gye.getContact(owner)
                        contact = gye.getContact(gyeMID)
                        grouplist = gye.getGroupIdsJoined()
                        contactlist = gye.getAllContactIds()
                        blockedlist = gye.getBlockedContactIds()
                        ret_ = "╭════════╬♥\n"
                        ret_ += "\n╠ akun : {}".format(contact.displayName)
                        ret_ += "\n╠ group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ teman : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blokir : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╰════════╬♥\n"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'เชคค่า':
                    try:
                        ret_ = "   ♥ Status Bots ♥\n ╭════════╬♥\n"
                        if settings["protect"] == True: ret_ += "║͜͡☆➣ Protect ✅"
                        else: ret_ += "║͜͡☆➣  Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n║͜͡☆➣ Qr Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n║͜͡☆➣ Invite Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n║͜͡☆➣ Cancel Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n║͜͡☆➣ Auto Add ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n║͜͡☆➣ Auto Join ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n║͜͡☆➣ Auto Leave ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n║͜͡☆➣ Auto Read ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n║͜͡☆➣ Check Sticker ✅"
                        else: ret_ += "\n║͜͡☆➣ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n║͜͡☆➣ Detect Mention ✅"
                        else: ret_ += "\n║͜͡☆➣ Detect Mention ❌"
                        ret_ += "\n╰════════╬♥\n"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
                        
                elif msg.text.lower().startswith("spaminvite "):
                   #if msg._from in admin:
                    dan = text.split("|")
                    userid = dan[0]
                    namagrup = dan[0]
                    jumlah = int(dan[0])
                    grups = gye.groups
                    tgb = gye.findContactsByUserid(userid)
                    if jumlah <= 10000000:
                        for var in range(0,jumlah):
                            try:
                                gye.createGroup(str(namagrup), [tgb.mid])
                                for i in grups:
                                    grup = gye.getGroup(i)
                                    if grup.name == namagrup:
                                        gye.inviteIntoGroup(grup.id, [tgb.mid])
                                        gye.sendMessage(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                            except Exception as Nigga:
                                gye.sendMessage(to, str(Nigga))
                            #else:
                                gye.sendMessage(to, "@! kebanyakan njer!!", [sender])
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("owneradd "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nAdd\nExecuted")
                            except:
                                pass
                    
                elif msg.text.lower().startswith("ownerdel "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nRemove\nExecuted")
                            except:
                                pass
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
                elif text.lower() == 'pt on':
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันลบแล้วครับเจ้านาย")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันลบแล้วครับเจ้านาย")
                                
                elif text.lower() == 'pt off':
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันลบแล้วครับเจ้านาย")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันลบแล้วครับเจ้านาย")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qr on':
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันเปิดลิ้งแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันเปิดลิ้งแล้วครับเจ้านาย")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันเปิดลิ้งแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันเปิดลิ้งแล้วครับเจ้านาย")
                                
                elif text.lower() == 'qr off':
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันเปิดลิ้งแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันเปิดลิ้งแล้วครับเจ้านาย")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันเปิดลิ้งแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันเปิดลิ้งแล้วครับเจ้านาย")
#-------------------------------------------------------------------------------
                elif text.lower() == 'iv on':
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันเชิญแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันเชิญแล้วครับเจ้านาย")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันเชิญแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันเชิญแล้วครับเจ้านาย")
                                
                elif text.lower() == 'iv off':
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันเชิญแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันเชิญแล้วครับเจ้านาย")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันเชิญแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันเชิญแล้วครับเจ้านาย")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cc on':
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันยกเลิกค้างเชิญแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันยกเลิกค้างเชิญแล้วครับเจ้านาย")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันยกเลิกค้างเชิญแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ เปิดป้องกันยกเลิกค้างเชิญแล้วครับเจ้านาย")
                                
                elif text.lower() == 'cc off':
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันยกเลิกค้างเชิญแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันยกเลิกค้างเชิญแล้วครับเจ้านาย")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันยกเลิกค้างเชิญแล้วครับเจ้านาย")
                            else:
                                gye.sendMessage(msg.to,"➲ ปิดป้องกันยกเลิกค้างเชิญแล้วครับเจ้านาย")
#-------------------------------------------------------------------------------
                elif text.lower() == 'pro on':
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        settings["joinsettings"] = True
                        settings["autoRead"] = True
                        settings["autoLeave"] = True
                        settings["autoJoinTicket"] = True
                        gye.sendMessage(msg.to,"เปิดป้องกันเข้าร่วมลิ้ง")
                        gye.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        gye.sendMessage(msg.to,"เปิดป้องกันลบ")
                        gye.sendMessage(msg.to,"เปิดป้องกันเชิญ")
                        gye.sendMessage(msg.to,"เปิดป้องกันยกเลิกค้างเชิญ")
                        gye.sendMessage(msg.to,"➲ เปิดระบบป้องกันทั้งหมดแล้วครับเจ้านาย")
                        		            
                elif text.lower() == 'pro off':
             #       if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        gye.sendMessage(msg.to,"ปิดป้องกันเข้าร่วมลิ้ง")
                        gye.sendMessage(msg.to,"ปิดป้องกันลบ")
                        gye.sendMessage(msg.to,"ปิดป้องกันเชิญ")
                        gye.sendMessage(msg.to,"ปิดป้องกันยกเลิกค้างเชิญ")
                        gye.sendMessage(msg.to,"➲ ปิดระบบป้องกันทั้งหมดแล้วครับเจ้านาย")
            #        else:
             #           gye.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'join on':
             #     if msg._from in Owner:    
                    settings["autoJoin"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'join off':
                #  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'leave on':
               #   if msg._from in Owner:
                    settings["autoLeave"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'leave off':
             #     if msg._from in Owner:
                    settings["autoLeave"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'sticker on':
                    settings["checkSticker"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'sticker off':
                    settings["checkSticker"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'dm on':
                    settings["datectMention"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'dm off':
                    settings["datectMention"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'link on':
                    settings["autoJoinTicket"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Join Link")
                elif text.lower() == 'link off':
                    settings["autoJoinTicket"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Join Link")                    
#==============================================================================#
                elif msg.text.lower() == 'บอท':
                        ais.sendContact(to, aisMID)
                        ais.sendMessage(msg.to,"➲ 1 อยู่ครับเจ้านาย")
                        ki2.sendContact(to, ki2MID)
                        ki2.sendMessage(msg.to,"➲ 2  อยู่ครับเจ้านาย")
                        ki3.sendContact(to, ki3MID)
                        ki3.sendMessage(msg.to,"➲ 3  อยู่ครับเจ้านาย")
                        ki4.sendContact(to, ki4MID)
                        ki4.sendMessage(msg.to,"➲ 4  อยู่ครับเจ้านาย")
                        ki5.sendContact(to, ki5MID)
                        ki5.sendMessage(msg.to,"➲ 5  อยู่ครับเจ้านาย")
                        ki6.sendContact(to, ki6MID)
                        ki6.sendMessage(msg.to,"➲ 6  อยู่ครับเจ้านาย")
                        ki7.sendContact(to, ki7MID)
                        ki7.sendMessage(msg.to,"➲ 7  อยู่ครับเจ้านาย")
                        ki8.sendContact(to, ki8MID)
                        ki8.sendMessage(msg.to,"➲ 8  อยู่ครับเจ้านาย")
                        ki9.sendContact(to, ki9MID)
                        ki9.sendMessage(msg.to,"➲ 9  อยู่ครับเจ้านาย")
                        ki10.sendContact(to, ki10MID)
                        ki10.sendMessage(msg.to,"➲ 10  อยู่ครับเจ้านาย")
                        ki11.sendContact(to, ki11MID)
                        ki11.sendMessage(msg.to,"➲ 11  อยู่ครับเจ้านาย")
                        ki12.sendContact(to, ki12MID)
                        ki12.sendMessage(msg.to,"➲ 12  อยู่ครับเจ้านาย")
                        ki13.sendContact(to, ki12MID)
                        ki13.sendMessage(msg.to,"➲ 13  อยู่ครับเจ้านาย")
                        ki14.sendContact(to, ki12MID)
                        ki14.sendMessage(msg.to,"➲ 14  อยู่ครับเจ้านาย")
                        ki15.sendContact(to, ki12MID)
                        ki15.sendMessage(msg.to,"➲ 15  อยู่ครับเจ้านาย")
                        ki16.sendContact(to, ki12MID)
                        ki16.sendMessage(msg.to,"➲ 16  อยู่ครับเจ้านาย")
                        ki17.sendContact(to, ki12MID)
                        ki17.sendMessage(msg.to,"➲ 17  อยู่ครับเจ้านาย")
                        ki18.sendContact(to, ki12MID)
                        ki18.sendMessage(msg.to,"➲ 18  อยู่ครับเจ้านาย")
                        ki19.sendContact(to, ki12MID)
                        ki19.sendMessage(msg.to,"➲ 19  อยู่ครับเจ้านาย")
                        ki20.sendContact(to, ki12MID)
                        ki20.sendMessage(msg.to,"➲ 20  อยู่ครับเจ้านาย")
                elif text.lower() in ["ออก."]:
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
                    ki5.leaveGroup(msg.to)
                    ki6.leaveGroup(msg.to)
                    ai7.leaveGroup(msg.to)
                    ki8.leaveGroup(msg.to)
                    ki9.leaveGroup(msg.to)
                    ki10.leaveGroup(msg.to)
                    ki11.leaveGroup(msg.to)
                    ki12.leaveGroup(msg.to)
                    ki13.leaveGroup(msg.to)
                    ki14.leaveGroup(msg.to)
                    ki15.leaveGroup(msg.to)
                    ki16.leaveGroup(msg.to)
                    ki17.leaveGroup(msg.to)
                    ki18.leaveGroup(msg.to)
                    ki19.leaveGroup(msg.to)
                    ki20.leaveGroup(msg.to)
                elif text.lower() in ["บาย."]:    
                    gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
                    ki5.leaveGroup(msg.to)
                    ki6.leaveGroup(msg.to)
                    ai7.leaveGroup(msg.to)
                    ki8.leaveGroup(msg.to)
                    ki9.leaveGroup(msg.to)
                    ki10.leaveGroup(msg.to)
                    ki11.leaveGroup(msg.to)
                    ki12.leaveGroup(msg.to)
                    ki13.leaveGroup(msg.to)
                    ki14.leaveGroup(msg.to)
                    ki15.leaveGroup(msg.to)
                    ki16.leaveGroup(msg.to)
                    ki17.leaveGroup(msg.to)
                    ki18.leaveGroup(msg.to)
                    ki19.leaveGroup(msg.to)
                    ki20.leaveGroup(msg.to)
                elif text.lower() in ["เข้ามา."]:    
                    G = gye.getGroup(msg.to)
                    ginfo = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    gye.updateGroup(G)
                    invsend = 0
                    Ticket = gye.reissueGroupTicket(msg.to)
                    ais.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    gye.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    gye.updateGroup(G)
                
                elif text.lower() == 'คท':
                    sendMessageWithMention(to, gyeMID)
                    gye.sendContact(to, gyeMID)
                elif text.lower() == 'มิด':
                    gye.sendMessage(msg.to,"[MID]\n" +  gyeMID)
                elif text.lower() == 'ชื่ิอ':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'ตัส':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'รูป':
                    me = gye.getContact(gyeMID)
                    gye.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'รูปวีดีโอ':
                    me = gye.getContact(gyeMID)
                    gye.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'รูปปก':
                    me = gye.getContact(gyeMID)
                    cover = gye.getProfileCoverURL(gyeMID)    
                    gye.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("คท "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            mi_d = contact.mid
                            gye.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("มิด "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        gye.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ชื่อ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ตัส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("รูป "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("รูปวีดีโอ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus + "/vp"
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("รูปปก "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = gye.getProfileCoverURL(ls)
                                gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            gye.cloneContactProfile(contact)
                            gye.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            gye.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':    
                    try:
                        gyeProfile.displayName = str(myProfile["displayName"])
                        gyeProfile.statusMessage = str(myProfile["statusMessage"])
                        gyeProfile.pictureStatus = str(myProfile["pictureStatus"])
                        gye.updateProfileAttribute(8, gyeProfile.pictureStatus)
                        gye.updateProfile(gyeProfile)
                        gye.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        gye.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    gye.sendContact(to, mmid)
                elif msg.text.lower().startswith("เพิ่มพิมตาม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            gye.sendMessage(msg.to,"เพิ่มคนพิมตามแล้วครับเจ้านายʕ•ᴥ•ʔ")
                            break
                        except:
                            nadya.sendMessage(msg.to,"เพิ่มคนพิมตามแล้วครับเจ้านายʕ•ᴥ•ʔ")
                            break
                elif msg.text.lower().startswith("ลบพิมตาม "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            gye.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'รายชื่อพิมตาม':
                    if settings["mimic"]["target"] == {}:
                        gye.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+gye.getContact(mi_d).displayName
                        gye.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "พิมตาม" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            gye.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            gye.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif msg.text.lower().startswith("พูด "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    gye.sendAudio(msg.to,"hasil.mp3")
                elif msg.text.lower().startswith("เขียน "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    gye.sendImageWithURL(msg.to, urlnya)
#==============================================================================#
                elif text.lower() == 'คนสร้างห้อง':
                    group = gye.getGroup(to)
                    GS = group.creator.mid
                    gye.sendContact(to, GS)
                elif text.lower() == 'ไอดีห้อง':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = gye.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อห้อง':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'ลิ้งห้อง':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = gye.reissueGroupTicket(to)
                            gye.sendMessage(to, "[ ลิ้งกลุ่มนี้ครับเจ้านาย ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            gye.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == '#เปิดลิ้ง':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            gye.sendMessage(to, "เปิดลิ้งห้องให้แล้วครับเจ้านาย")
                        else:
                            group.preventedJoinByTicket = False
                            gye.updateGroup(group)
                            gye.sendMessage(to, "เปิดลิ้งห้องให้แล้วครับเจ้านาย")
                elif text.lower() == '#ปิดลิ้ง':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            gye.sendMessage(to, "ปิดลิ้งห้องให้แล้วครับเจ้านาย")
                        else:
                            group.preventedJoinByTicket = True
                            gye.updateGroup(group)
                            gye.sendMessage(to, "ปิดลิ้งห้องให้แล้วครับเจ้านาย")
                elif text.lower() == 'เชคห้อง':
                    group = gye.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(gye.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลห้อง ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ คนสร้างห้อง : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ by,maibotline ]"
                    gye.sendMessage(to, str(ret_))
                    gye.sendImageWithURL(to,)
                elif text.lower() == 'รายชื่อคนในห้อง':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        ret_ = "╔══[ รายชื่อคนในห้อง ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ มี {} คนครับเจ้านาย ]".format(str(len(group.members)))
                        gye.sendMessage(to, str(ret_))
                elif text.lower() == 'รายชื่อห้อง':
                        groups = gye.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = gye.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        gye.sendMessage(to, str(ret_))
#-------------------------------------------------------------------------------
                elif text.lower() == 'ล้างแบน':
                        settings["blacklist"] = {}
                        gye.sendMessage(msg.to,"➲ Done")
                        gye.sendMessage(msg.to,"➲ ล้างหมดแล้วครับเจ้านาย")
                        
                elif text.lower() == 'เชคบอท':
                        gye.sendMessage(msg.to,"➲ เริ่มเลยนะครับเจ้านาย")
                        ais.sendMessage(msg.to,"➲ 1 มาครับเจ้านาย")
                        ki2.sendMessage(msg.to,"➲ 2  มาครับเจ้านาย")
                        ki3.sendMessage(msg.to,"➲ 3  มาครับเจ้านาย")
                        ki4.sendMessage(msg.to,"➲ 4  มาครับเจ้านาย")
                        ki5.sendMessage(msg.to,"➲ 5  มาครับเจ้านาย")
                        ki6.sendMessage(msg.to,"➲ 6  มาครับเจ้านาย")
                        ki7.sendMessage(msg.to,"➲ 7  มาครับเจ้านาย")
                        ki8.sendMessage(msg.to,"➲ 8  มาครับเจ้านาย")
                        ki9.sendMessage(msg.to,"➲ 9  มาครับเจ้านาย")
                        ki10.sendMessage(msg.to,"➲ 10  มาครับเจ้านาย")
                        ki11.sendMessage(msg.to,"➲ 11  มาครับเจ้านาย")
                        ki12.sendMessage(msg.to,"➲ 12  มาครับเจ้านาย")
                        ki13.sendMessage(msg.to,"➲ 13  มาครับเจ้านาย")
                        ki14.sendMessage(msg.to,"➲ 14  มาครับเจ้านาย")
                        ki15.sendMessage(msg.to,"➲ 15  มาครับเจ้านาย")
                        ki16.sendMessage(msg.to,"➲ 16  มาครับเจ้านาย")
                        ki17.sendMessage(msg.to,"➲ 17  มาครับเจ้านาย")
                        ki18.sendMessage(msg.to,"➲ 18  มาครับเจ้านาย")
                        ki19.sendMessage(msg.to,"➲ 19  มาครับเจ้านาย")
                        ki20.sendMessage(msg.to,"➲ 20  มาครับเจ้านาย")
                        gye.sendMessage(msg.to,"➲ มาครบครับเจ้านาย")
                        
                elif text.lower() == 'แบน':
                        settings["wblacklist"] = True
                        gye.sendMessage(msg.to,"ลง Contact")
                        
                elif msg.text in ["unbancontact"]:
                        settings["dblacklist"] = True
                        gye.sendMessage(msg.to,"ลง Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'เชคแบน':
                        if settings["blacklist"] == {}:
                            gye.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            gye.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="═══T E R S A N G K A═══"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, gye.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n═══T E R S A N G K A═══\n\nTotal Tersangka :  %i" % len(settings["blacklist"])
                            gye.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text.lower().startswith("เตะ "):
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(GUE).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(GUE).sendText(msg.to,"Error")
                elif "เตะดึง " in msg.text:
                        vkick0 = msg.text.replace("เตะดึง ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = gye.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    gye.kickoutFromGroup(msg.to,[target])
                                    gye.findAndAddContactsByMid(target)
                                    gye. inviteIntoGroup(msg.to,[target])
                                except:
                                    pass
#-------------------------------------------------------------------------------
                elif text.lower() == 'ciak all member':
                 #   if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
                            _name = msg.text.replace("kickallmember","")
                            #gs = gye.getGroup(msg.to)
                            gs = ais.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
                            gs = ki3.getGroup(msg.to)
                            gs = ki4.getGroup(msg.to)
                            gs = ki5.getGroup(msg.to)
                            gs = ki6.getGroup(msg.to)
                            gs = ki7.getGroup(msg.to)
                            gs = ki8.getGroup(msg.to)
                            gs = ki9.getGroup(msg.to)
                            gs = ki10.getGroup(msg.to)
                            gs = ki11.getGroup(msg.to)
                            gs = ki12.getGroup(msg.to)
                           #gye.sendMessage(msg.to,"「 Bye All 」")
                           #gye.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                gye.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,ais,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    gye.sendMessage(msg.to,"") 
#==============================================================================#          
                elif text.lower() == 'แทค':
                    group = gye.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        gye.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        gye.sendMessage(to, "จำนวลสมาชิกในกลุ่ม {} คนครับเจ้านาย".format(str(len(nama))))          
                elif text.lower() == 'เปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                gye.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            gye.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'ปิดอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        gye.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        gye.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'ลบเวลาอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        gye.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        gye.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'คนอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            gye.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = gye.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            gye.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        gye.sendMessage(receiver,"Lurking has not been set.")
                        
#===============================================================================[gyeMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] GYEVHA BOTS KICK")
            try:
                if op.param3 in gyeMID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
#                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki2MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki3MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki4MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[kiMID gyeMID]
                if op.param3 in aisMID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki5MID:
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ginfo = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki3MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki6MID:
                        G = ki6.getGroup(op.param1)
                        ginfo = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        ginfo = ki6.getGroup(op.param1)
                        ki6.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki4MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki7MID:
                        G = ki7.getGroup(op.param1)
                        ginfo = ki7.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki7.updateGroup(G)
                        invsend = 0
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)
                        ginfo = ki7.getGroup(op.param1)
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki7.updateGroup(G)
                        invsend = 0
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki7.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki2MID gyeMID]
                if op.param3 in ki2MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID kiMID]
                elif op.param3 in ki2MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ki.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki3MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki4MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki3MID gyeMID]
                if op.param3 in ki3MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID kiMID]
                elif op.param3 in ki3MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki2MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki4MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki4MID gyeMID]
                if op.param3 in ki4MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID kiMID]
                elif op.param3 in ki4MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki2MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki3MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#

#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ais.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ais.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    gye.sendMessage(op.param1,"Jangan Buka Qr")
            else:
                gye.sendMessage(op.param1,"")
#==============================================================================#
       # if op.type == 55:
        #    print ("[ 55 ] GYEVHA BOTS EMPAT")
         #   if op.param1 in read["readPoint"]:
          #      _name = gye.getContact(op.param2).displayName
           #     tz = pytz.timezone("Asia/Jakarta")
           #     timeNow = datetime.now(tz=tz)
            #    timeHours = datetime.strftime(timeNow," (%H:%M)")
             #   read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
     #   backupData()
    #except Exception as error:
     #   logError(error)
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if text.lower() == '/ti/g/':    
                if settings["join ticket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = gye.findGroupByTicket(ticket_id)
                        gye.acceptGroupInvitationByTicket(group.id,ticket_id)
                        gye.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        gye.acceptGroupInvitation(op.param1)
        ais.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
        ki3.acceptGroupInvitation(op.param1)
        ki4.acceptGroupInvitation(op.param1)
        ki5.acceptGroupInvitation(op.param1)
        ki6.acceptGroupInvitation(op.param1)
        ki7.acceptGroupInvitation(op.param1)
        ki8.acceptGroupInvitation(op.param1)
        ki9.acceptGroupInvitation(op.param1)
        ki10.acceptGroupInvitation(op.param1)
        ki11.acceptGroupInvitation(op.param1)
        ki12.acceptGroupInvitation(op.param1)
        ki13.acceptGroupInvitation(op.param1)
        ki14.acceptGroupInvitation(op.param1)
        ki15.acceptGroupInvitation(op.param1)
        ki16.acceptGroupInvitation(op.param1)
        ki17.acceptGroupInvitation(op.param1)
        ki18.acceptGroupInvitation(op.param1)
        ki19.acceptGroupInvitation(op.param1)
        ki20.acceptGroupInvitation(op.param1)

    except Exception as e:
        gye.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        gye.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
