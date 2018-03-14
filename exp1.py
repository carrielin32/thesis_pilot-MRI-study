
import sys
import random
# sys.path.append('../../')
sys.path = ['../../']+sys.path

from expy import *
import math
import numpy as np
from random import gauss
import pandas as pd 
from pandas import Series, DataFrame
#import neuropsydia as n 

start(fullscreen=False,mouse_visible=True,sample_rate=44100)
#n.start()

#dataleft = {"ISI":[]}

def whitenoise(length,power_signal,snr=-8.0):

    #import power_signal & try 
    
    sample_rate=22050
    
    #zero_time = int(sample_rate * 0.01)
    grow_time = int(sample_rate * 0.5)
    #end_zero_time = int(sample_rate * 1)
    
    #zero_series = [gauss(0.0, 0.0) for i in range(zero_time)]#1.3s
    grow_series = [gauss(0.0, 1.0) for i in range(grow_time)]#2.7s
    #end_zero_series = [gauss(0.0, 0.0) for i in range(end_zero_time)]
    
    factor = [logn(x,grow_time) for x in list(range(1,grow_time + 1))]
    
    #make a logrithm curve from 1.3s to 4s 
    for i in range(grow_time):
        
        for _ in range(6):    #'_' for throwaway variables 
            
            grow_series[i] *= factor[i]
    
    max_series = [gauss(0.0, 1.0) for i in range(int(sample_rate * 0.5))]
    
    series = grow_series + max_series #+ end_zero_series
    
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


def raisedecayx(data, raise_duration, decay_duration, sr):
        raise_sample = int(raise_duration * sr*2)
        decay_sample = int(decay_duration * sr*2) #sr=sample_rate 

        data_t = data[:]
        #sr=22050 
        for i in range(len(data)):
            if i in range(0,raise_sample):
                data_t[i] = int(data_t[i]*np.cos(np.linspace(np.pi/2,np.pi,raise_sample))[i])
            elif i in range(len(data)-decay_sample,len(data)):
                data_t[i] = int(data_t[i]*np.cos(np.linspace(0,np.pi/2,decay_sample))[i-(len(data)-decay_sample)])
        return data_t


def compare_syllable(data):
    v = (data['syllable']).values
    return (v[:-1] != v[1:]).all()

def conditional_sample(data, predicate, *args, **kwargs):
    d = data.sample(*args, **kwargs)
    while not predicate(d):
        d = data.sample(*args, **kwargs)
    return d


def trial(stim):

    #ISI= random.randrange(start=2, stop=6, step=1)  # Select the inter-stimuli interval (ISI)

    drawText('+') #visual cue here (task?)
    show(0.5)
    clear()

    sound = loadSound('test/data/1syllable/' + stim['stimuli'] + '.WAV',stereo_array_format=True)  # Load the wav file
    #sound = changeOnTracks(sound,changeVolume,[1,0]) #play only through left ear
    sound_noise = whitenoise(length=len(sound), power_signal=power(sound),snr= -8.0)
    sound_final = sound + sound_noise
    sound_final = raisedecayx(sound_final, raise_duration=0.01, decay_duration=0.01, sr=44100)

    playSound(sound_final )  # Play the wav file

        
    print(stim['stimuli']) #the presentation stimuli 
    
    key,RT = waitForResponse({key_.F: 'ba', key_.G: 'bi', key_.H: 'da',key_.J: 'di'}) # Waiting for pressing 'FGHJ'
    # four-button key pad needed 

    clear()
    show(random.randrange(start=2, stop=4, step=1))  #ISI 

    return key,RT

def block(blockID):

    #drawText('*')  #make this one bigger (font size=40, bold)
    #show(10)
    #clear()

    #readStimuli('test/data/trial_list_snr.csv', query='block==%s' %(blockID))
    #stimuli= readStimuli('test/data/trial_list_snr.csv', query='block==%s' %(blockID))
    #random.shuffle(stimuli)  #use optseq2 to generate random list 
    #print(stimuli) #print the shuffle list 

    data=pd.read_csv('test/data/trial_list_snr.csv',names=['stimuli','syllable','block'])
    data=DataFrame(data,columns=['stimuli','syllable','block'])


    data_final=data.pipe(conditional_sample, compare_syllable, frac=1)

    data_final.to_csv('/Users/carrielin/Desktop/finalsample.csv')

    readStimuli('/Users/carrielin/Desktop/finalsample.csv', query='block==%s' %(blockID))
    data=readStimuli('/Users/carrielin/Desktop/finalsample.csv', query='block==%s' %(blockID))
    #data_random=randombycolumn(df=data) #just a list!!not a dataframe 

    #print(data['stimuli'])

    alert('Print "S" to start the experiment', allowed_keys=[key_.S])
    
    result= []
    for t in stimuli:
        result.append(trial(t))

    saveResult(result,stim=stimuli)


    #clear()
    #drawText('*')
    #show(20)


shared.subject = getInput('please enter the subject ID:')

instruction(shared.setting['instruction4'])


for blockID in range(4): #five blocks in total 
    block(blockID+1)


alertAndQuit('Finished! Thanks for your participation :)')
