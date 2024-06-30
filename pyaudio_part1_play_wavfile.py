import struct
import pyaudio
from scipy.fftpack import fft
import wave
import sys
import os
import numpy as np
import time
from tkinter import TclError
from pylab import get_current_fig_manager
import matplotlib.pyplot as plt

class AudioFile:


    def __init__(self, file):
        """ Initiate audio stream """ 
        self.p = pyaudio.PyAudio()
        self.chunk = 1024*2
        self.channels = 1
        self.format = pyaudio.paInt16
        self.rate = 84100
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.format,
            channels = self.channels,
            rate = self.rate,
            output = True
        )

    def play(self):
        """ Play wav file """
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)
            data

    def close(self):
        """ shutdown """ 
        self.stream.close()
        self.p.terminate()

# Usage example for pyaudio
a = AudioFile("./jello.wav")
a.play()
a.close()
