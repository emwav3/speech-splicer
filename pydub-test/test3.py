import time, configparser
from pydub import AudioSegment
from pydub.utils import make_chunks, db_to_float

splicing_resolution = 10
silence_threshold = 430
pause_threshold = 60


def main():
    # Load audio file and print the length
    audio = AudioSegment.from_wav("MB Track 3.wav")
    print("audio length:\t\t" + str(audio.__len__() / 1000) + "seconds")

    #Strip off the first few seconds and create chunks of audio
    audio = audio[4000:]
    chunks = make_chunks(audio, splicing_resolution)
    chuck_start_end_list = []
    running = True
    average_loudness = audio.rms
    silence_threshold = average_loudness * db_to_float(-19)
    print("chunk list length:\t" + str(len(chunks)))
    print("silence threshold:\t" + str(silence_threshold))

    build = audio[:0]
    i = 0
    while i < (len(chunks)):
        start_stop = [0, 0]
        if chunks[i].rms < silence_threshold:
            while chunks[i].rms <= silence_threshold:
                i += 1
            start_stop[0] = i
        else:
            while chunks[i].rms >= silence_threshold:
                i += 1
                print("test")
        start_stop[1] = i
        # print("pass")
        chuck_start_end_list.append(start_stop)
    # build = chunk_list[i]
    #     build.export(("test/test{0}.mp3".format(str(i))), format="mp3")
    # build.export("test2.mp3", format="mp3")
    print(len(chuck_start_end_list))

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time:\t\t\t\t%s seconds" % str(time.time() - start_time))