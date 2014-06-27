

import time, configparser
from pydub import AudioSegment
from pydub.utils import make_chunks, db_to_float

splicing_resolution = 50
silence_threshold = 430
pause_threshold = 10

def average_loudness(audio):
    average_loudness = audio.rms
    return average_loudness

def main():
    x = pause_threshold
    audio = AudioSegment.from_wav("MB Track 1.wav")
    audio = audio[3000:]
    chunks = make_chunks(audio, splicing_resolution)
    build = audio[:0]
    silence_threshold = audio.rms * db_to_float(-16)
    resets = 0
    chunk_list = []
    for i in range(len(chunks)):

        if chunks[i].rms < silence_threshold:
            # if(i == 0):
            #     chunk_list.append(build)
            if (0 < x):
                x -= 1
                print("decrement x")
            else:
                x = pause_threshold
                print("reset x")
                resets += 1
                chunk_list.append(build)
                build = audio[:0]

        else:

            build += chunks[i]
    build = audio[:0]
    print(len(chunk_list))
    for i in range(len(chunk_list)):
        print("ex")
        build = chunk_list[i]
        build.export(("test/test{0}.mp3".format(str(i))), format="mp3")
    print("resets: " + str(resets))
    build.export("test2.mp3", format="mp3")

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % str(time.time() - start_time))