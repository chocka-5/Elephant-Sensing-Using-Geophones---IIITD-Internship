import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import soundfile as sf

from scipy import signal
from matplotlib import pyplot as plt
y, rate = sf.read('human65b.wav')
a=len(y)
y = y[0:a] * signal.blackmanharris(a)
X_amp = np.abs(np.fft.rfft(y))
X_db = 20 * np.log10(X_amp)
freqs = np.fft.rfftfreq(a, 1/rate)
plt.plot(freqs, X_db)
plt.show()