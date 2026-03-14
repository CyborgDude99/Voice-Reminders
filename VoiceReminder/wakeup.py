# To be executed at 6:30 am
# Called from cron job
"""
Place the minute, hour, day of the month, month of the year, and day of the week, and then the command you wish to run, in that order. Must be run in the pi interface.
https://phoenixnap.com/kb/set-up-cron-job-linux
"""
# Variables
ModelName = "./glados.onnx"
Voiceline1 = "We hope you have had a wonderful rest! Time to face the morning rush. Please wake up and go eat some food."


# Clear state: Reset button pressed
# Load model
import wave
from piper import PiperVoice
voice = PiperVoice.load(ModelName)

# Generate wav file
with wave.open("wakeup.wav", "wb") as wav_file:
        voice.synthesize_wav(Voiceline1, wav_file)
# Play wav file
