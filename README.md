# Operos Genomas - chinese whispers 

## 1. Install pyaudio
Debian/Ubuntu
Use the package manager to install PyAudio:
```
sudo apt-get install python-pyaudio python3-pyaudio
```
If the latest version of PyAudio is not available, install it using pip:
```
pip install pyaudio
```
Notes:

pip will download the PyAudio source and build it for your system. Be sure to install the portaudio library development package (portaudio19-dev) and the python development package (python-all-dev) beforehand.
For better isolation from system packages, consider installing PyAudio in a virtualenv.



## 2. Install GPIOzero on Raspberry Pi
GPIO Zero is packaged in the apt repositories of Raspberry Pi OS, Debian and Ubuntu. It is also available on PyPI.

### 2.1 apt
First, update your repositories list:
```
pi@raspberrypi:~$ sudo apt update
```
Then install the package for Python 3:
```
pi@raspberrypi:~$ sudo apt install python3-gpiozero
```
or Python 2:
```
pi@raspberrypi:~$ sudo apt install python-gpiozero
```

### 2.2 pip
If you’re using another operating system on your Raspberry Pi, you may need to use pip to install GPIO Zero instead. Install pip using get-pip and then type:
```
pi@raspberrypi:~$ sudo pip3 install gpiozero
```
or for Python 2:
```
pi@raspberrypi:~$ sudo pip install gpiozero
```
To install GPIO Zero in a virtual environment, see the Development page.

### 2.3 PC/Mac
In order to use GPIO Zero’s remote GPIO feature from a PC or Mac, you’ll need to install GPIO Zero on that computer using pip. See the Configuring Remote GPIO page for more information.
