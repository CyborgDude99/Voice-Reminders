import wave
from piper import PiperVoice
voice = PiperVoice.load("./glados.onnx")
with wave.open("test2.wav", "wb") as wav_file:
        voice.synthesize_wav("Rock and Stone- wait, what am I saying", wav_file)