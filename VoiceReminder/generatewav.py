import wave
from piper import PiperVoice
voice = PiperVoice.load("./glados.onnx")
with wave.open("test2.wav", "wb") as wav_file:
        voice.synthesize_wav("Sixty percent of the time, it works every time.", wav_file)