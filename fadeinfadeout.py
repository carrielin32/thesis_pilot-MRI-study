
#demo 
#useful for uncompressed wav. file 

import numpy as np 
from scipy.io import wavfile 

def fadeInOutSound(srcSoundFile, dstSoundFile): 

	sampleRate, soundData = wavfile.read(srcSoundFile) #read sound file 

	start = len(soundData)//3 
	soundData = soundData[start:-start]   #extract middle 1/3 of the sound 

	length = len(soundData)
	n = 10 
	start = length//n      #fadein 1/10 of the current sound, and fadeout 1/10 of the sound also 

	factors = tuple(map(lambda num: round(num/start,1), range(start)))
	factors = factors + (1,)*(length-start*2)+factors[::-1]  #2nd parameter in round(), control the speed of fadein-fadeout

	soundData = np.array(tuple(map(lambda data, factor: [np.int16(data[0]*factor), 
														np.int16(data[1]*factor)], soundData, factors)))

	wavfile.write(dstSoundFile, sampleRate, soundData)

	fadeInOutSound ('name_original.wav', 'name_final.wav')


	#cut-off (weaken-time)
	def cut_offx(data):
		weaken_sample = int(weaken_duration * sr) #sr=sample_rate 
		data_t = data[:int(sr* duration_target)]

		return np.concatenate(
			[data_t[:-weaken_sample], 
			data_t[-weaken_sample:] * np.cos(np.linspace(0, np.pi/2, weaken_sample))]) #weaken last weaken duration of the sound 




