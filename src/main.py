from pygame._sdl2 import get_audio_device_names
from pygame import mixer
from mutagen.mp3 import MP3
import time
from get_audio_device import get_output_device
import pyautogui

audio_device = get_output_device()

mixer.quit()
mixer.init(devicename=audio_device)
audio = MP3("../remarks/fuck_you_1.mp3")
mixer.music.load('../remarks/fuck_you_1.mp3')
mixer.music.play()
time.sleep(float(audio.info.length)+.25)
mixer.music.stop()

