# Elephant Sensing Using Geophones


Elephant accidents near railway tracks are increasing year by year. The objective of the project is to detect the elephant's footsteps and raising an alarm
to avoid the accident. The footsteps generate seismic waves in the ground in different patterns which can be used to classify the animals based on their
footsteps.

Seismic sensors are the devices used to measure seismic vibrations by converting ground motion into a measurable electronic signal. To detect the seismic
waves, we had to choose geophone.

Output from the geophone sensor comes in ranges of microvolts. The circuit was designed that will amplify the signal and filter out the noise.It was designed 
in PCB using Eagle Software.

We saved the signal in the form of a .wav file. In order to extract the features from the audio signal to train the ML model, we used PyAudioAnalysis
library which gave us around 68 features for a single audio file.We developed the SVM model ,tested and classified the datasets.

