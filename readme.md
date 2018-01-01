# pyAudioStream

#### Pentesting audio capture with Python 2.7

### Dependencies:
• Must install portaudio:

    brew install portaudio
_location: `/usr/local/Cellar/portaudio/19.6.0/`_

• Must install pyaudio:

    pip install pyaudio

### Server:

##### Example Usage:
**Server**:

    python3 serverAudio.py IP PORT

**Client**

    python3 clientAudio.py IP PORT

replace `IP` and `PORT` with their respective values

This should also work for Python 2, but the print statements and encoding/decoding might need to be changed.

##### Will make a setup file for this to automate silently