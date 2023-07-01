from pygame import mixer
from mutagen.mp3 import MP3
import time
import pyautogui
import pydirectinput
import config.config as config
from get_audio_device import get_output_device
from select_remark import remark
from detect_death import did_you_die_though
from detect_tf2 import detect_active_tf2
from exit_routine import clean_up_and_exit

def main():
    start = time.time()
    path = config.tf2_console_log_path
    audio_device = get_output_device()

    mixer.quit()
    mixer.init(devicename=audio_device)
    last_death_index = 0

    while True:
        death, last_death_index = did_you_die_though(path, last_death_index)
        print(death, last_death_index)
        if death == True:
            selected_remark = remark()
            audio = MP3(selected_remark)
            mixer.music.load(selected_remark)
            time.sleep(3)
            pydirectinput.keyDown('v')
            mixer.music.play()
            time.sleep(float(audio.info.length)+.25)
            mixer.music.stop()
            pydirectinput.keyUp('v')
            time.sleep(2)

        elapsed = time.time()-start
        if elapsed % 60 > 55:
            if detect_active_tf2() == False:
                clean_up_and_exit(path)
                break


main()

