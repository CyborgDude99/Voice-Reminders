# To be executed at 6:30 am
# Called from cron job
"""
Place the minute, hour, day of the month, month of the year, and day of the week, and then the command you wish to run, in that order. Must be run in the pi interface.
https://phoenixnap.com/kb/set-up-cron-job-linux
"""

# Imports
import wave
import logging
import sys
from timeit import default_timer as timer
from piper import PiperVoice
from pygame import mixer 



# Variables
ModelName = "./glados.onnx"
Voiceline1 = "We hope you have had a wonderful rest! Time to face the morning rush. Please wake up and go eat some food."
WavFile = "wakeup.wav"
INITIALSTATE = 1
WAITINGINITIALSTATE = 2
SHUTDOWNSTATE = 99
CurrentState = INITIALSTATE


# Clear state: Reset button pressed
# Load model

voice = PiperVoice.load(ModelName)
mixer.init()
logging.basicConfig(
    level = logging.INFO, 
    stream= sys.stdout
)
logger = logging.getLogger(__name__)
running = True

# Generate wav file
with wave.open(WavFile, "wb") as wav_file:
        voice.synthesize_wav(Voiceline1, wav_file)

start = timer()
while running: 
        if CurrentState == INITIALSTATE:
                logger.info("In initial state")
                mixer.music.load(WavFile)
                mixer.music.play()
                CurrentState = WAITINGINITIALSTATE
        if CurrentState == WAITINGINITIALSTATE:
                # Has enough time passed?
                logger.info("In waiting initial state")
                if timer() - start >= 10:
                        CurrentState = SHUTDOWNSTATE 
        if CurrentState == SHUTDOWNSTATE:
                logger.info("In shutdown state")
                running = False                           


