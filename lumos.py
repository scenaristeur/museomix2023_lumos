import time
from pymata4 import pymata4
import os 
import vlc

count=0
trigpin=11
ecopin=12

plouf_Is_reading = False

plouf_player = vlc.MediaPlayer("51 Tailleurs de pierres qui tapent sur une pierre.m4a")

board = pymata4.Pymata4()

# def readPlouf():
#     playsound.playsound("plouf.mp3", True)


def callbackSR04_1(data):
    global count
    print("distance ", data[2])
    if data[2] < 20 :
        plouf_player.play()
    #else:
        #plouf_player.pause()
        #plouf_player.stop()

        

   



board.set_pin_mode_sonar(trigpin, ecopin, callbackSR04_1)
#count=0
while True:
    try: 
        time.sleep(0.1)
       # print("is reading",plouf_Is_reading)
        if plouf_Is_reading == False :
            #print("read")
            board.sonar_read(trigpin)
    except Exception:
        board.shutdown()

