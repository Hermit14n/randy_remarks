from pygame._sdl2 import get_audio_device_names
from pygame import mixer
from mutagen.mp3 import MP3
import time
import pyautogui
mixer.init()

audio_devices = get_audio_device_names()
print(audio_devices)
audio_device = [x for x in audio_devices if x == 'CABLE Input (VB-Audio Virtual Cable)']

if len(audio_device) == 1:
    audio_device = audio_device[0]
    print(f"VB Cable input audio device found: {audio_device}")
elif len(audio_device) == 0:
    raise ValueError("No VBAUDIO Cable input found, install VBAUDIO: https://www.vb-audio.com/Cable/")
else:
    raise ValueError("More than one VBAUDIO Cable input found, that's weird...")

mixer.quit()
mixer.init(devicename=audio_device)
audio = MP3("../remarks/fuck_you_1.mp3")
mixer.music.load('../remarks/fuck_you_1.mp3')
mixer.music.play()
time.sleep(float(audio.info.length)+.25)
mixer.music.stop()

