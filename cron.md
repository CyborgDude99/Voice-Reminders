## Cron settings for Voice Reminders
The cron settings for the Wakeup voice reminder are:
```
38 11 * * 0,1,2,3,4,5,6 cd /home/alex/VoiceReminder/; /home/alex/.venv/bin/python wakeup.py > /home/alex/wakeup.log
```