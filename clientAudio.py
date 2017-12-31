import socket
import pyaudio as pa
import wave

#record
CHUNK = 1024
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10 # This takes priority over the serverAudio

HOST = '127.0.0.1'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

p = pa.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

#print("*recording")

frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
 data  = stream.read(CHUNK)
 frames.append(data)
 s.sendall(data)

#print("*done recording")

stream.stop_stream()
stream.close()
p.terminate()
s.close()

#print("*closed")
