import sys
# sys.path.append('../../')
sys.path = ['../../']+sys.path

from expy import *

start(fullscreen=False,mouse_visible=True,sample_rate=44100)

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
        # data_decay= np.concatenate([data_t[:-decay_sample], data_t[-decay_sample:-1]* np.cos(np.linspace(0, np.pi/2,decay_sample))])

        # data_t_2 = data_decay[:int(sr * duration_target)]

        # data_decay_raise= np.concatenate([data_t_2[raise_sample:]*np.sin(np.linspace(0, np.pi/2, raise_sample))], data_t_2[raise_sample:])
 


sound = loadSound('test/data/1syllable/' + 'ba1' + '.WAV',stereo_array_format=True)  # Load the wav file
# print(sound)
sound_final = raisedecayx(sound, raise_duration=0.01, decay_duration=0.01, sr=44100)
playSound(sound_final)  # Play the wav file
alertAndQuit('')