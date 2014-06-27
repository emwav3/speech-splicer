import time, configparser
from pydub import AudioSegment
from pydub.utils import make_chunks, db_to_float

splicing_resolution = 30
silence_threshold = 430
pause_threshold = 60


def main():
    x = pause_threshold
    audio = AudioSegment.from_wav("MB Track 3.wav")
    audio = audio[4000:]
    chunks = make_chunks(audio, splicing_resolution)
    build = audio[:0]
    print(silence_threshold)
    resets = 0
    chunk_list = []
    running = True
    index = 0
    while running:
        if chunks[i].rms < silence_threshold:
            index += 1
            else (chunks[index].rms < pause_threshold):
            while (chunks[index].rms < silence_threshold):
                build += chunks[index]

                build = audio[:0]

        else:

            print("decrement x")
        x -= 1

    else:

        build += chunks[i]


build = audio[:0]
print(len(chunk_list))
for i in range(1, len(chunk_list)):
    print("ex")
    build = chunk_list[i]
    build.export(("test/test{0}.mp3".format(str(i))), format="mp3")
print("resets: " + str(resets))
build.export("test2.mp3", format="mp3")
print("silence threshold: " + str(silence_threshold))

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time: %s seconds" % str(time.time() - start_time))