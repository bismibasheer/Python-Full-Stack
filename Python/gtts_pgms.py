from gtts import gTTS
import os
s=gTTS(text="hello",slow=False,lang="en")
s.save("sample_audio.mp3")
os.system('start sample_audio.mp3')