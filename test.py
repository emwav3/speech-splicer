from pydub.effects import strip_silence

__author__ = 'S511181'
from functools import reduce

from pydub import AudioSegment
from pydub.utils import db_to_float
from pydub.utils import make_chunks
from pydub import effects
from pydub import silence


def main():
    audio = AudioSegment.from_wav("track2.wav")
    average_loudness = audio.rms
    audio = audio[:7500]
    print(average_loudness)
    silence_threshold = average_loudness * db_to_float(-10)
    print(silence_threshold)

    parts = (ms for ms in audio if ms.rms > silence_threshold)
    print("t")
    audio = reduce(lambda a, b: a + b, parts)
    print("e")
    audio.export("test.wav", format="wav")


def strip():
    audio = AudioSegment.from_mp3("track2.mp3")
    audio = audio[:30000]
    audio = strip_silence(audio, 300, -16, 0)
    audio.export("test.mp3", format="mp3")


def chunks():
    audio = AudioSegment.from_mp3("track2.mp3")
    audio = audio
    chunks = make_chunks(audio, 200)
    empty = audio[:0]
    for chunk in chunks:
        if chunk.rms > 430:
            empty += chunk
    empty.export("test.mp3", format="mp3")


if __name__ == '__main__':
    # import timeit
    # print(timeit.timeit("main()", setup="from __main__ import main"))
    import time

    start_time = time.time()
    chunks()
    print("--- %s seconds ---" % str(time.time() - start_time))


