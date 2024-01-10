import pyaudio as ad
import struct
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


chunk = 8096  # Increased chunk size for better low-frequency representation
obs = ad.paInt16
fps = 44100

p = ad.PyAudio()
stream = p.open(format=obs, channels=1, rate=fps, input=True, output=True, frames_per_buffer=chunk)
fig, ax = plt.subplots()
ax.set_facecolor((0.0, 0.0, 0.0))
freq = np.fft.fftfreq(chunk, d=1/fps)[:chunk//2]  # Frequency values for the FFT
line, = ax.plot(freq, np.random.rand(chunk//2), color="White")
ax.set_ylim(0, 100000)
ax.set_xlim(200, 2000)
ax.set_ylabel('Amplitude')
ax.set_xlabel('Frequency(Hz)')
def update(frame):
    data = stream.read(chunk)  # Byte data
    audio_signal = np.array(struct.unpack(str(2 * chunk) + 'B', data), dtype="b")[::2] + 130
    spectrum = np.fft.fft(audio_signal)[:chunk//2]
    line.set_ydata(np.abs(spectrum))
    plt.pause(0.001)
    return line,

# Create the animation
animation = FuncAnimation(fig, update, interval=50, blit=True)

# Display the plot
plt.show()
