# v1.0 = If PyAudio instance can be reused and not terminated after each file is created

import  pyaudio
import  wave
from    gpiozero    import Button

button = Button(2)              # GPIO 

is_recording = False            # control flag
counter      = 1                # number of wav file

form_1      = pyaudio.paInt16   # 16-bit resolution
chans       = 1                 # 1 channel
samp_rate   = 44100             # 44.1kHz sampling rate
chunk       = 4096              # 2^12 samples for buffer
record_secs = 6               # seconds to record
dev_index   = 2                 # device index found by p.get_device_info_by_index(ii)

wav_output_filename = 'telephone_' # name of .wav file

audio = pyaudio.PyAudio() # create pyaudio instantiation

print("sample rate")
print(audio.get_device_info_by_index(2)['defaultSampleRate'])
print(audio.get_device_info_by_index(2))


def callback(in_data, frame_count, time_info, status):
    mic_audio = numpy.fromstring(in_data,dtype=numpy.int16)
    return (mic_audio, pyaudio.paContinue)

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
mic_audio = numpy.empty((self.buffersize),dtype="int16")

while True:
    if button.is_pressed:
        print("Stop recording")
    else:
        print("Start recording")
        # create pyaudio stream

        print("recording")
        frames = []

        # loop through stream and append audio chunks to frame array
        for ii in range(0,int((samp_rate/chunk)*record_secs)):
            # data = stream.read(chunk)
            data = mic_audio
            frames.append(data)
            if button.is_pressed:
                break

        print("finished recording")

        # stop the stream, close it, and terminate the pyaudio instantiation
        stream.stop_stream()
        stream.close()
        # audio.terminate()

        # save the audio frames as .wav file
        filename = wav_output_filename + counter + ".wav"
        wavefile = wave.open(filename,'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()


audio.terminate()
