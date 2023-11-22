# v1.0 = If PyAudio instance can be reused and not terminated after each file is created

import  pyaudio
import  wave
import  numpy
import  time
import  pygame
from    gpiozero    import Button
import time

button = Button(2)              # GPIO 

is_recording = False            # control flag
counter      = 1                # number of wav file

form_1      = pyaudio.paInt16   # 16-bit resolution
chans       = 1                 # 1 channel
samp_rate   = 44100             # 44.1kHz sampling rate
chunk       = 4096              # 2^12 samples for buffer
record_secs = 60*30             # seconds to record
dev_index   = 1                 # device index found by p.get_device_info_by_index(ii)

output_dir = '/home/pi/operos-genomas/records'
PROMPT = '/home/pi/operos-genomas/pradzia.mp3'
HANG_UP = '/home/pi/operos-genomas/pakeltas.mp3'

prompts = ['/home/pi/operos-genomas/Fragmentas1.mp3','/home/pi/operos-genomas/Fragmentas2.mp3','/home/pi/operos-genomas/Fragmentas3.mp3',]

print("Creating instance of PyAudio:")
audio = pyaudio.PyAudio() # create pyaudio instance

print("Device used:")
print(audio.get_device_info_by_index(dev_index))

def callback(in_data, frame_count, time_info, status):
    mic_audio = numpy.fromstring(in_data,dtype=numpy.int16)
    frames.append(mic_audio)
    return (mic_audio, pyaudio.paContinue)

def record():
    stream = audio.open(format   = form_1,
                        rate     = samp_rate,
                        channels = chans,
                        input_device_index  = dev_index,
                        input    = True,
                        frames_per_buffer   =chunk,
                        stream_callback = callback)

    start_time = time.time()

    while (time.time()-start_time <= record_secs):
        if button.is_pressed:
            break

    pygame.mixer.music.stop()

    stream.stop_stream()
    stream.close()
    filename = output_dir+'/'+str(int(time.time())) + ".wav"

    wavefile = wave.open(filename,'wb')   
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

    print("File saved as: ", filename)

    counter += 1
    frames = []



"""
Setting up the array that will handle the timeseries of audio data from our input
"""
mic_audio = numpy.empty((chunk),dtype="int16")

frames = []

animation = "|/-\\"
idx = 0

pygame.mixer.init()

i = 0

while True:
    if button.is_pressed:
#        print("Lift the button to start recording", animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.5)

    else:

        pygame.mixer.music.load(prompts[i])
        pygame.mixer.music.play()
        i = i + 1
        if i >= len(prompts):
            i = 0

        # record()

        while not button.is_pressed:
            # if not pygame.mixer.music.get_busy():
            #     pygame.mixer.music.load(HANG_UP)
            #     pygame.mixer.music.play()
            time.sleep(1)

        pygame.mixer.music.stop()

audio.terminate()
