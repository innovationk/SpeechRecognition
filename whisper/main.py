import whisper

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe audio file
def transcribe_audio(audio_file_path):
    result = model.transcribe(audio_file_path)
    return result['text']

# Example usage
audio_file_path = './samples/mininalLong.wav'
text = transcribe_audio(audio_file_path)
print(text)