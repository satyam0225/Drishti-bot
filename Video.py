import time 

import vlc
media = vlc.MediaPlayer('filename')
media.play()

time.sleep(10)



def playvideo():

    media.play()

    time.sleep(10)


def pause():
    media.pause()


