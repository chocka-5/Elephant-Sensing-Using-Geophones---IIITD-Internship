import pyAudioAnalysis
#import matplotlib.pyplot as plt
#import audioBasicIO as au
#import audioFeatureExtraction as afe
import audioTrainTest as aT
#[Fs,X] = au.readAudioFile('voice.wav')
#afe.mtFeatureExtractionToFileDir('/home/chocka', 1, 1, 0.050, 0.5)
#aT.featureAndTrain(["/home/chocka/humandata/Final_reading","/home/chocka/humandata/cycle" ,"/home/chocka/humandata/Blank"],1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm_rbf", "humancycle")
[Result, P, classNames]=aT.fileClassification("/home/chocka/cte.wav","humancycle","svm_rbf")
#print (Result)
print (P)
print (classNames)
#source ./env/bin/activate