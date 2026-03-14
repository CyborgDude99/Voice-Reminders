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
import time
from timeit import default_timer as timer
from piper import PiperVoice
from pygame import mixer
from time import sleep 



# Variables
ModelName = "./glados.onnx"
Voiceline1 = "We hope you have had a wonderful rest! Time to face the morning rush. Please wake up and go eat some food."
Voiceline2 = "What is taking you so long? Why are you forcing me to wait like this?"
Voiceline3 = "Thank you, test subject. Shutting down."
WavFile1 = "wakeup.wav"
WavFile2 = "angry.wav"
WavFile3 = "sleep.wav"
TimerDelay = 10
INITIALSTATE = 1
WAITINGINITIALSTATE = 2
ESCALATEDSTATE = 3
WAITINGESCALATEDSTATE = 4
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
with wave.open(WavFile1, "wb") as wav_file:
        voice.synthesize_wav(Voiceline1, wav_file)
with wave.open(WavFile2, "wb") as wav_file:
        voice.synthesize_wav(Voiceline2, wav_file)
with wave.open(WavFile3, "wb") as wav_file:
        voice.synthesize_wav(Voiceline3, wav_file)

while running: 
        if CurrentState == INITIALSTATE:
                logger.info("In initial state")
                mixer.music.load(WavFile1)
                mixer.music.play()
                start = timer()
                CurrentState = WAITINGINITIALSTATE
        if CurrentState == WAITINGINITIALSTATE:
                # Has enough time passed?
                if timer() - start >= TimerDelay:
                        CurrentState = ESCALATEDSTATE
        if CurrentState == ESCALATEDSTATE: 
                logger.info("In escalated state")
                mixer.music.load(WavFile2)
                mixer.music.play()
                start = timer()
                CurrentState = WAITINGESCALATEDSTATE
        if CurrentState == WAITINGESCALATEDSTATE:
                # Has enough time passed?
                if timer() - start >= TimerDelay:
                        CurrentState = SHUTDOWNSTATE
        if CurrentState == SHUTDOWNSTATE:
                logger.info("In shutdown state")
                mixer.music.load(WavFile3)
                mixer.music.play()
                time.sleep(6)
                running = False                           


