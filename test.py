from pygame._sdl2 import get_audio_device_names
from pygame import mixer
mixer.init()

audio_devices = get_audio_device_names()
audio_device = [x for x in audio_devices if x == 'CABLE Input (VB-Audio Virtual Cable)']
if len(audio_device) == 1:
    audio_device = audio_device[0]
    print(f"VB Cable input audio device found: {audio_device}")
elif len(audio_device) == 0:
    raise ValueError("No VBAUDIO Cable input found, install VBAUDIO: https://www.vb-audio.com/Cable/")
else:
    raise ValueError("More than one VBAUDIO Cable input found, that's weird...")

