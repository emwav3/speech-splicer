author__ = 'S511181'
from pydub import AudioSegment

audio = AudioSegment.from_mp3("track2.mp3")

audio.export("track2.wav", format="wav")