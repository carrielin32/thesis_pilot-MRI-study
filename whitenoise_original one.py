import math
import numpy as np
from random import gauss

def whitenoise(length,power_signal,snr=-12.0):

    
    sample_rate = 88200
    
    zero_time = int(sample_rate * 1.30) #rise/decay
    grow_time = int(sample_rate * 2.70)
    #end_zero_time = int(sample_rate * 1)
    
    zero_series = [gauss(0.0, 0.0) for i in range(zero_time)]#1.3s
    grow_series = [gauss(0.0, 1.0) for i in range(grow_time)]#2.7s
    #end_zero_series = [gauss(0.0, 0.0) for i in range(end_zero_time)]
    
    factor = [logn(x,grow_time) for x in list(range(1,grow_time + 1))]
    
    #make a logrithm curve from 1.3s to 4s 
    for i in range(grow_time):
        
        for _ in range(6):  
            
            grow_series[i] *= factor[i]
    
    max_series = [gauss(0.0, 1.0) for i in range(int(sample_rate * (length - 4)))]
    
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



#record stimuli 
#start()  # Initiate the experiment environment

#noise_level = environmentNoise(0.5)  # Detect the noise level of environment

#'Without file'
#textSlide('Recording: ')
#sound = recordSound(noise_level, rec_length_min=2, sound_length_max=4)
#textSlide('Playing: ')
#playSound(sound)

#'With file'
#textSlide('Recording to file: ')
#recordSound(noise_level, rec_length_min=2, sound_length_max=4, path='data/record.WAV')
#record = loadSound('data/record.WAV')
#textSlide('Playing from file: ')
#playSound(record)





