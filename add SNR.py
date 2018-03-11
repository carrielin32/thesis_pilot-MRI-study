
import sys
import random
# sys.path.append('../../')
sys.path = ['../../']+sys.path

from expy import *
import math
import numpy as np
from random import gauss


start(fullscreen=False,mouse_visible=True,sample_rate=22050)


def whitenoise(length,power_signal,snr=-8.0): #snr 

    
    sample_rate=22050
    
    zero_time = int(sample_rate * 0.01)
    grow_time = int(sample_rate * (len(sound)-0.01))
    #end_zero_time = int(sample_rate * 1)
    
    zero_series = [gauss(0.0, 0.0) for i in range(zero_time)]#10ms
    grow_series = [gauss(0.0, 1.0) for i in range(grow_time)]#last 10ms
    #end_zero_series = [gauss(0.0, 0.0) for i in range(end_zero_time)]
    
    factor = [logn(x,grow_time) for x in list(range(1,grow_time + 1))]
    
    #make a logrithm curve from 1.3s to 4s 
    for i in range(grow_time):
        
        for _ in range(6):    #'_' for throwaway variables 
            
            grow_series[i] *= factor[i]
    
    max_series = [gauss(0.0, 1.0) for i in range(int(sample_rate * len(sound)))]
    
    series = zero_series + grow_series + max_series #+ end_zero_series
    
    power_noise_ideal = power_signal / (10 ** (snr/10))
    
    power_noise = power(max_series)
    
    ratio = math.sqrt(power_noise_ideal / power_noise)
    
    for i in range(len(series)):
        series[i] = ratio * series[i]
    
    samples = np.array(series, dtype='int16')
#note parallel the dtype of stimuli & noise 

    return samples

def logn(x,n):
    #change: return a log(n) function
    return math.log(x, n)
    
def power(array):
    power = 0.0
    for i in array:
        power += (i ** 2) / len(array)
    return power

def risedecayx(data, weaken_duration, duration_target):
        weaken_sample = int(weaken_duration * sr) #sr=sample_rate 
        data_t = data[:int(sr* duration_target)]

        sr=22050 

        return np.concatenate(
            [data_t[:weaken_sample] * np.sin(np.linspace(0, np.pi/2, weaken_sample),data_t[weaken_sample:-weaken_sample],   
            data_t[-weaken_sample:] * np.cos(np.linspace(0, np.pi/2, weaken_sample)))]) #weaken last weaken duration of the sound 


sound = loadSound('test/data/task1/' + stim['stimuli'] + '.WAV',stereo_array_format=True)  # Load the wav file
sound_noise = whitenoise(length=len(sound), power_signal=power(sound),snr= -8.0) #snr
sound_final = sound + sound_noise
sound_final = risedecayx(sound_final, weaken_duration=0.01, duration_target=len(sound_final))

playSound(sound_final)  # Play the wav file

        