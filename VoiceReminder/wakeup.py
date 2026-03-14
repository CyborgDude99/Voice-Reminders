# To be executed at 6:30 am
# Called from cron job
"""
Place the minute, hour, day of the month, month of the year, and day of the week, and then the command you wish to run, in that order. Must be run in the pi interface.
https://phoenixnap.com/kb/set-up-cron-job-linux
"""

# Imports
import wave
from timeit import default_timer as timer
from piper import PiperVoice


# Variables
ModelName = "./glados.onnx"
Voiceline1 = "We hope you have had a wonderful rest! Time to face the morning rush. Please wake up and go eat some food."
INITIALSTATE = 1
WAITINGINITIALSTATE = 2
SHUTDOWNSTATE = 99

CurrentState = INITIALSTATE

# Clear state: Reset button pressed
# Load model

voice = PiperVoice.load(ModelName)

# Generate wav file
with wave.open("wakeup.wav", "wb") as wav_file:
        voice.synthesize_wav(Voiceline1, wav_file)

start = timer()

while CurrentState != SHUTDOWNSTATE:
        if CurrentState == INITIALSTATE:
                # Play wav file 1
                CurrentState = WAITINGINITIALSTATE
        if CurrentState == WAITINGINITIALSTATE:
                # Has enough time passed?
                if timer() - start >= 10:
                        CurrentState = SHUTDOWNSTATE             


