# v1.0 = If PyAudio instance can be reused and not terminated after each file is created

import  pyaudio
import  wave
import  numpy
import  time
from    gpiozero    import Button

button = Button(2)              # GPIO 

is_recording = False            # control flag
counter      = 1                # number of wav file

form_1      = pyaudio.paInt16   # 16-bit resolution
chans       = 1                 # 1 channel
samp_rate   = 44100             # 44.1kHz sampling rate
chunk       = 4096              # 2^12 samples for buffer
record_secs = 60               # seconds to record
dev_index   = 2                 # device index found by p.get_device_info_by_index(ii)

wav_output_filename = 'telephone_' # name of .wav file

print("Creating instance of PyAudio:")
audio = pyaudio.PyAudio() # create pyaudio instance

print("Device used:")
print(audio.get_device_info_by_index(2))

def callback(in_data, frame_count, time_info, status):
    mic_audio = numpy.fromstring(in_data,dtype=numpy.int16)
    frames.append(mic_audio)
    return (mic_audio, pyaudio.paContinue)


print("Creating audio stream")
stream = audio.open(format   = form_1,
                            rate     = samp_rate,
                            channels = chans,
                            input_device_index  = dev_index,
                            input    = True,
                            frames_per_buffer   =chunk,
                            stream_callback = callback)

"""
Setting up the array that will handle the timeseries of audio data from our input
"""
mic_audio = numpy.empty((chunk),dtype="int16")

frames = []

animation = "|/-\\"
idx = 0

while True:
    if button.is_pressed:
        print("Lift the button to start recording", animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
        # print("Lift the button to start recording", end='\r')
    else:
        print()
        print("Recording")
        start_time = time.time()

        while (time.time()-start_time <= record_secs):
            """
            Record for "record_secs" number of seconds and check if stop button has been pressed to scape earlier 
            and stop recording.
            """
            if button.is_pressed:
                break


        print("finished recording")

        # stop the stream, close it, and terminate the pyaudio instantiation
        stream.stop_stream()
        stream.close()
        # audio.terminate()

        # save the audio frames as .wav file
        filename = wav_output_filename +str(counter) + ".wav"
        # with open(filename,"wb") as wavefile:
        wavefile = wave.open(filename,'wb')   
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()

        print("File saved as: ", filename)

        # Increment the count for the filename
        counter += 1

        # comment this line out in production for the script to loop forever
        # break

audio.terminate()
