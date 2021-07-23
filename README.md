# Operos Genomas - chinese whispers 

## 1. Install pyaudio
Debian/Ubuntu
Use the package manager to install PyAudio:

sudo apt-get install python-pyaudio python3-pyaudio
If the latest version of PyAudio is not available, install it using pip:

pip install pyaudio
Notes:

pip will download the PyAudio source and build it for your system. Be sure to install the portaudio library development package (portaudio19-dev) and the python development package (python-all-dev) beforehand.
For better isolation from system packages, consider installing PyAudio in a virtualenv.
