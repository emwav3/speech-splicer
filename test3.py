import time

from pydub import AudioSegment
from pydub.utils import make_chunks, db_to_float
import pandas as pd
from pandas import DataFrame, Series


splicing_resolution = 10
silence_threshold = 800
pause_threshold = 300


def main():
    # Load audio file and print the length
    audio = AudioSegment.from_wav("C:\MB Track 32.wav")
    print("audio length:\t\t" + str(audio.__len__() / 1000) + "seconds")

    # Strip off the first few seconds and create chunks of audio
    # audio = audio[4000:]


    chuck_start_end_list = []
    running = True
    average_loudness = audio.rms
    # silence_threshold = average_loudness * db_to_float(-21)
    chunks = make_chunks(audio, splicing_resolution)
    print("chunk list length:\t" + str(len(chunks)))

    build = audio[:0]
    i = 0
    start = 0
    stop = 0
    while i < (len(chunks)):
        start_stop = [0, 0]
        if chunks[i].rms <= silence_threshold:
            while i < (len(chunks)) and chunks[i].rms <= silence_threshold:
                print("low" + str(i))
                print(chunks[i].rms)
                i += 1
            start = i
        else:
            while i < (len(chunks)) and chunks[i].rms > silence_threshold:
                print("high" + str(i))
                print(chunks[i].rms)
                i += 1
        stop = i
        # print("pass")
        if ( start != stop):
            chuck_start_end_list.append([start, stop])
    # build = chunk_list[i]
    #     build.export(("test/test{0}.mp3".format(str(i))), format="mp3")
    # build.export("test2.mp3", format="mp3")


    print((chuck_start_end_list))
    print("Chuck start stop list length: " + str(len(chuck_start_end_list)))
    print("silence threshold:\t" + str(silence_threshold))

    # For testing only -- prints segment sizes, showing larger segment
    large_chunks = 0
    for chunk in chuck_start_end_list:
        size = (chunk[1] - chunk[0])

        if size > 32:
            print("----------" + str(size))
            large_chunks += 1
        else:
            print(size)
    print(large_chunks)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:\t\t\t\t%s seconds" % str(time.time() - start_time))
    print(db_to_float(10))