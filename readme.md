## Voice Reminder System
When reinstalling on new pie, use pip install piper-tts to install Piper into the Pi.
Uses the venv/bin/activate command to create a virtual environment in which audio commands will run
The cd VoiceReminder command is used to select the directory
Then, the aplay -D hw:0,0 test(or any other voiceline).wav command is run. 
Still working on the simpler aplay test.wav command
Need to install pygame with pip install pygame