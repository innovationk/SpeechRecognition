from vosk import Model, KaldiRecognizer
import wave
import json

# Download from https://alphacephei.com/vosk/models
model_path = './vosk/vosk-model-en-us-0.22'
model = Model(model_path)

def read_audio_file(audio_file_path):
    with wave.open(audio_file_path, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
    return buffer, rate

def transcribe_audio(audio_file_path):
    buffer, rate = read_audio_file(audio_file_path)
    recognizer = KaldiRecognizer(model, rate)
    recognizer.AcceptWaveform(buffer)
    result = recognizer.Result()
    text = json.loads(result)['text']
    return text

audio_file_path = './samples/mininalLong.wav'
text = transcribe_audio(audio_file_path)
print(text)