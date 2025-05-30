# -*- coding: utf-8 -*-
"""
Created on Sun May 11 12:49:32 2025

@author: 一只狐狸
"""

import numpy as np
from scipy.io.wavfile import write
import os

frequency = 2400.0
duration = 15.0
sample_rate = 16000

t = np.linspace(0, duration, int(sample_rate * duration), False)
audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)

audio_data_int = np.int16(audio_data * 32767)
write("2.4kHz_sound.wav", sample_rate, audio_data_int)