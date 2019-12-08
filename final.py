import time
from pydub import AudioSegment
import pyAudioAnalysis
import audioTrainTest as aT
import wave
import contextlib
from datetime import *
fmt='%Y-%m-%d-%H-%M-%S_{fname}'
def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        print ("loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed)) 
        time.sleep(1)  
        

#stopwatch(10)
fname = 'result1.wav'
count = 0
#with contextlib.closing(wave.open(fname,'r')) as f:
	#frames = f.getnframes()
    #rate = f.getframerate()
 #   d = frames / float(rate)
  #  d=int(d*1000)

for t1 in range (0,1800000,1000):
	t2 = t1 +10000
	newAudio = AudioSegment.from_wav(fname)
	newAudio = newAudio[t1:t2]
	newAudio.export('newtest.wav', format="wav")
	[Result, P, classNames]=aT.fileClassification("/home/chocka/newtest.wav","humancycle","svm_rbf")
	f=open("/home/chocka/result5.txt",'a')

	P[0]=int(P[0]*100)
	P[1]=int(P[1]*100)
	count =count +1
	if (P[0] >70):
		f.write(str(count))
		f.write("--\t")
		f.write("human")
		f.write('\n')
		#f.write(datetime.now().strftime(fmt))
		#f.write('\n')

	elif (P[1] > 70):
		f.write(str(count))
		f.write("--\t")
		f.write("cycle")
		f.write('\n')
		#f.write(datetime.now().strftime(fmt))
		#f.write('\n')		

