__author__ = 'S511181'
from functools import reduce
import pydub
from pydub import AudioSegment
from pydub.utils import db_to_float

audio = AudioSegment.from_wav("track2.wav")
audio = audio
average_loudness = audio.rms
silence_threshold = average_loudness * db_to_float(-16)
print(silence_threshold)

parts = pydub.utils.make_chunks(audio, 100)
print("t")
for part in parts:
    if part.rms > silence_threshold:
        audio.append(part)


print("e")
audio.export("test.wav", format="wav")