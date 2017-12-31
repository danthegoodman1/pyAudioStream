s# Echo server program
import socket
import pyaudio as pa
import wave
import time
from time import gmtime, strftime

CHUNK = 1024
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10 # clientAudio record seconds takes priority over this
WAVE_OUTPUT_FILENAME = "server_output"
WIDTH = 2
frames = []

p = pa.PyAudio()
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)


HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
data = conn.recv(1024)

i=1
try:
    while data != b'':
        if i == 1:
            print("Client connected from {0}".format(addr))
            i +=1
        stream.write(data)
        data = conn.recv(1024)
        # Debug Stuff
        # i=i+1
        # print(i)
        # print(data)
        frames.append(data)
except KeyboardInterrupt:
    wf = wave.open('{f_n}-from-{ip}-at-{time}.wav'.format(
        f_n=WAVE_OUTPUT_FILENAME,
        ip=addr[0],
        time=strftime("%Y-%m-%d %H:%M:%S", gmtime())), 'wb')

    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print("File written out to: {f_n}-from-{ip}-at-{time}.wav".format(
        f_n=WAVE_OUTPUT_FILENAME,
        ip=addr[0],
        time=strftime("%Y-%m-%d %H:%M:%S", gmtime())))
    print(addr)

    stream.stop_stream()
    stream.close()
    p.terminate()
    conn.close()

wf = wave.open('{f_n}-from-{ip}-at-{time}.wav'.format(
    f_n=WAVE_OUTPUT_FILENAME,
    ip=addr[0],
    time=strftime("%Y-%m-%d %H:%M:%S", gmtime())), 'wb')

wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
print("File written out to: {f_n}-from-{ip}-at-{time}.wav".format(
    f_n=WAVE_OUTPUT_FILENAME,
    ip=addr[0],
    time=strftime("%Y-%m-%d %H:%M:%S", gmtime())))

stream.stop_stream()
stream.close()
p.terminate()
conn.close()
