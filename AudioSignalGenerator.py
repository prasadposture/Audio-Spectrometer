import numpy as np
import scipy.io.wavfile as wav

def generate_mono_tone(duration, frequency, amplitude, sampling_rate=44100):
    t = np.arange(0, duration, 1/sampling_rate)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return signal

def generate_multi_tone(duration, frequencies, amplitudes, sampling_rate=44100):
    t = np.arange(0, duration, 1/sampling_rate)
    signal = np.sum([amplitude * np.sin(2 * np.pi * frequency * t) for frequency, amplitude in zip(frequencies, amplitudes)], axis=0)
    return signal

def save_wav(filename, signal, sampling_rate=44100):
    wav.write(filename, sampling_rate, signal.astype(np.int16))

# Example of generating a mono-tone signal
mono_tone_signal = generate_mono_tone(duration=15, frequency=730, amplitude=500.0)
save_wav("mono_tone.wav", mono_tone_signal)

# Example of generating a multi-tone signal
frequencies = [440, 880, 320]
amplitudes = [500, 400, 600]
multi_tone_signal = generate_multi_tone(duration=15, frequencies=frequencies, amplitudes=amplitudes)
save_wav("multi_tone.wav", multi_tone_signal)
