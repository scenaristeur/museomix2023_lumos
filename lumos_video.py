import time
from pymata4 import pymata4
import os 
import vlc
import pyautogui

count=0
trigpin=11
ecopin=12

plouf_Is_reading = False

VIDEO_PATH="test.mkv"

import psutil

current_process = psutil.Process()


def get_end_callback(mediaplayer):
    def end_callback(event):
        print("End of playing reached")
        mediaplayer.stop()
        mediaplayer.get_media().release()
        mediaplayer.release()
        mediaplayer.get_instance().release()
        os.system ("killall vlc")
    return end_callback



# media_player = vlc.MediaPlayer("test.mkv")


board = pymata4.Pymata4()

# def readPlouf():
#     playsound.playsound("plouf.mp3", True)

def play():
    vlc_instance = vlc.Instance(["--no-xlib"])
    media_player = vlc.MediaPlayer(vlc_instance, VIDEO_PATH)
    media_player.toggle_fullscreen()

    media_player.play()

    event_manager = media_player.event_manager()
    event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, get_end_callback(media_player))



#play()


def callbackSR04_1(data):
    global count
    print("distance ", data[2])
    children = current_process.children(recursive=True)
    for child in children:
        print('Child pid is {}'.format(child.pid))

    if data[2] < 20 :
        play()
        pyautogui.press('space')  
    # else:
    #     plouf_player.pause()
    #     plouf_player.stop()

        

   



board.set_pin_mode_sonar(trigpin, ecopin, callbackSR04_1)
#count=0
while True:
    try: 
        time.sleep(0.1)
        #print("is reading",plouf_Is_reading)
        if plouf_Is_reading == False :
            #print("read")
            board.sonar_read(trigpin)
    except Exception:
        board.shutdown()

